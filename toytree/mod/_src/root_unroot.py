#!/usr/bin/env python

r"""Class for rooting and unrooting of trees.

Rooting and unrooting trees turns out to be quite a bit more
complicated than you might expect. The difficult part is keeping
track of Node features that in practice are coded as attributes to
Nodes, but in reality are sometimes features of *edges*, such as
'support' or 'dist', and thus need to be re-assigned when an parent
child relationships change.

Re-rooting a rooted tree:
               o                            x
              / \                          / \
             1   2         root('n')      n   u
                / \          -->             / \
               .   u                        2   .
                  / \                      / \
                 .   n                    1   .

Rooting an unrooted tree:
                                            x
                                           / \
              _ 2 _        root('n')      n   u
             |  |  |         -->             / \
             1  .  u                        2   .
                  / \                      / \
                 .   n                    1   .

References
----------
- Czech, L., Huerta-Cepas, J. and Stamatakis, A. (2017) A critical
  review on the use of support values in tree viewers and
  bioinformatics toolkits. Molecular Biology and Evolution, 34,
  1535–1542. doi: 10.1093/molbev/msx055

Examples
--------
>>> # Test Case from Czech et al. 2017 (edge features)
>>> NEWICK = "((C,D)1,(A,(B,X)3)2,E)R;"
>>> tree = toytree.tree(NEWICK)
>>>
>>> # set a color feature to Nodes and 'ecolor' and 'ncolor'
>>> colors = {'1': 'red', '2': 'green', '3': 'orange'}
>>> tree.set_node_data("ecolor", colors, inplace=True)
>>> tree.set_node_data("ncolor", colors, inplace=True)
>>>
>>> # draw the trees
>>> kwargs = {
>>>     'layout': 'd', 'use_edge_lengths': False,
>>>     'node_sizes': 10, 'node_labels': 'name',
>>>     'node_labels_style': {
>>>         'font-size': 20,
>>>         'baseline-shift': 10,
>>>         '-toyplot-anchor-shift': 10,
>>>     }}
>>> tree.draw(
>>>     node_colors=tree.get_node_data('ncolor', missing='black'),
>>>     edge_colors=tree.get_node_data('ecolor', missing='black'),
>>>     **kwargs,
>>> )
>>>
>>> # re-root, treating 'ecolor' but not 'ncolor' as edge feat.
>>> rtree = tree.root("X", edge_features=["ecolor"])
>>> rtree.draw(
>>>     node_colors=rtree.get_node_data('ncolor', missing='black'),
>>>     edge_colors=rtree.get_node_data('ecolor', missing='black'),
>>>     **kwargs,
>>> );
"""
from typing import Optional, Sequence, TypeVar, Set
from loguru import logger
from toytree.core.node import Node
from toytree.utils import ToytreeError

logger = logger.bind(name="toytree")

# type aliases
ToyTree = TypeVar("ToyTree")
Query = TypeVar("Query", int, str, Node)


class Rooter:
    r"""Root ToyTree on Node query selection.

    See `toytree.mod.root` docstring for details.
    """
    def __init__(
        self,
        tree: ToyTree,
        *query: Query,
        regex: bool = False,
        root_dist: Optional[float] = None,
        edge_features: Optional[Sequence[str]] = None,
        ):

        self.tree = tree
        self.root_dist = root_dist
        self.node: Node = self._get_edge_to_split(*query, regex=regex)
        self.edge_features: Set = self._get_edge_features(edge_features)

    @staticmethod
    def _get_edge_features(edge_features):
        """Return the features associated with edges instead of nodes."""
        default = {'_dist', 'support'}
        disallowed = {"dist", "idx", "up", "children"}
        if edge_features is None:
            return default - disallowed
        if isinstance(edge_features, str):
            return (default | {edge_features}) - disallowed
        return (default | set(edge_features)) - disallowed

    def _get_edge_to_split(self, *query, regex) -> Node:
        """Return the Node below new root edge from input query.

        Get MRCA Node of the input selection. If it is the root, then
        get the MRCA of the inverse selection. If that is also root,
        then raise exception for bad selection.
        """
        nodes = self.tree.get_nodes(*query, regex=regex)
        mrca = self.tree.get_mrca_node(*nodes)

        # if mrca is root, try to get mrca of reciprocal.
        if mrca.is_root():
            nodes = set(self.tree.get_nodes()) - set(nodes) - set([mrca])
            # orig = mrca
            mrca = self.tree.get_mrca_node(*nodes)
            # if mrca.is_root():
                # raise ToytreeError(
                    # f"Bad selection to `root()`, cannot root on {orig}")
        # experimental: skip hybrid nodes from networks up to next node.
        # if self.node2.up and len(self.node2.children) == 1:
            # self.node2 = self.node2.up
            # self.node1 = self.node1.up
        logger.debug(f"rooting on mrca of nodes={nodes}")
        logger.debug(f"mrca={mrca}")
        return mrca

    def run(self):
        """Return ToyTree rooted on the input selection."""
        # if rooting on root of already rooted tree.
        if self.tree.is_rooted():
            if self.tree.treenode in [self.node, self.node.up]:
                return self.tree
            self.tree.unroot(inplace=True)
        self._insert_root_node()
        self.tree._update()
        return self.tree

    def _infer_max_support(self):
        """Get max support as 1.0 or 100 based on other Node values."""
        if max(i.support for i in self.tree.traverse()) > 1:
            return 100
        return 1.0

    def _insert_root_node(self):
        r"""Insert a new node to break an edge to create root.

        Important Nodes are:
            - oldroot: o
            - oldroot.children: 1,2
            - node: n
            - node.up: u
            - newroot: x

                   o                         x         polar = [u, 2]
                  / \                       / \        flip = [1]
                 1   2       root('n')     n   u
                    / \         -->           / \
                   .   u                     2   .
                      / x                   / \
                     .   n                 1   .

        oldroot is removed, newroot is created. All Nodes that are
        ancestors of u on the original tree are re-polarized.
        """
        # store references to Nodes before their relationships change.
        support = self._infer_max_support()
        newroot = Node(name="root", support=support, dist=0)
        edge = (self.node, self.node.up)

        # nodes on path from node to the original root.
        path = (self.node,) + self.node.get_ancestors() # [n, u, 2, o]

        # store edge features for re-polarizing edges in path.
        feats = {
            n: {i: getattr(n, i, None) for i in self.edge_features}
            for n in path
        }

        # polarize each node on path
        for idx in range(1, len(path)):           # [u, 2, o]    [3, 2, R]
            # connect this node to its new parent (previously child)
            node = path[idx]                      # u            R
            child = path[idx - 1]                 # n            2
            node._up = child                      # u -> n       R -> 2
            node._remove_child(child)             # n -x u       2 -x R

            # connect this node to its new child (previously parent)
            # if this node is not the former root node.
            if node != path[-1]:
                node._add_child(path[idx + 1])

            # transfer non-root edge features
            for feature in self.edge_features:
                value = feats[child][feature]
                if value is not None:
                    setattr(node, feature, value)
                else:
                    delattr(node, feature)

        # set node and its parent as sisters, and children of newroot.
        newroot._children = edge             # n -> x, u -> x
        edge[0]._up = newroot
        edge[1]._up = newroot

        # position of newroot on edge, None=midpoint, ...
        if self.root_dist is None:
            edge[0]._dist /= 2.
            edge[1]._dist /= 2.
        else:
            sumdist = sum(i.dist for i in edge)
            if self.root_dist > sumdist:
                raise ValueError(
                    "`root_dist` arg (placement of root node on existing edge) "
                    f"cannot be greater than length of the edge: {sumdist}.")
            edge[0]._dist = self.root_dist
            edge[1]._dist = sumdist - self.root_dist

        # update as ToyTree
        self.tree.treenode = newroot
        self.tree._update()
        return self.tree


def root(
    tree: ToyTree,
    *query: Query,
    regex: bool=False,
    root_dist: Optional[float] = None,
    edge_features: Optional[Sequence[str]] = None,
    inplace: bool=False) -> ToyTree:
    r"""Return a ToyTree rooted on the edge above selected Node query.

    Rooting a tree involves splitting and edge to insert a new Node.
    (It helps to think of it as pinching an edge and pulling it back
    to create a new root). The root Node is named "root" and has
    support of 100 (or 1.0, depending on support values) and dist=0.

    Example of rooting an unrooted tree:
                                                x
                                               / \
                  _ 2 _        root('n')      n   u
                 |  |  |         -->             / \
                 1  .  u                        2   .
                      / \                      / \
                     .   n                    1   .

    Example of re-rooting a rooted tree:
                   o                            x
                  / \                          / \
                 1   2         root('n')      n   u
                    / \          -->             / \
                   .   u                        2   .
                      / \                      / \
                     .   n                    1   .

    Parameters
    ----------
    tree: ToyTree
        A rooted or unrooted ToyTree to (re-)root.
    *query: str, int, or Node
        One or more Node selectors, which can be Node objects, names,
        or int idx labels. If multiple are entered the MRCA node will
        be used as the base of the edge to split.
    regex: bool
        If True then Node name strings are treated as regular
        expressions that can match to multiple Nodes.
    root_dist: None or float
        The length (dist) along the root edge above the Node query
        where the new root edge should be placed. Default is None
        which will place root at the midpoint of the edge. A float
        can be entered, but will raise ToyTreeError if > len of edge.
    edge_features: Sequence[str]
        One or more Node features that should be treated as a feature
        of its edge, not the Node itself. On rooting, edge features
        are re-polarized, to apply to the correct Node. The 'dist'
        and 'support' features are always treated as edge features.
        Add additional edge features here. See docs for example.
    inplace: bool
        If True the original tree is modified and returned, otherwise
        a modified copy is returned.

    Examples
    --------
    >>> tree = toytree.rtree.unittree(ntips=10, seed=123)
    >>> t1 = tree.root("r8", "r9")
    >>> t2 = tree.root("r8", "r9", root_dist=0.3)
    >>> toytree.mtree([t1, t2]).draw();
    """
    tree = tree if inplace else tree.copy()
    return Rooter(
        tree, *query,
        regex=regex, root_dist=root_dist, edge_features=edge_features,
        ).run()


def unroot(tree: ToyTree, inplace: bool = False) -> ToyTree:
    """Return an unrooted ToyTree by collapsing the root Node.

    This will convert a binary split into a multifurcation.
    The Node idx values change on unrooting because the number of
    Nodes has changed.

    Note
    ----
    The unrooting process is not destructive of information, you can
    re-root a tree on the same edge position as before to recover the
    same tree. The new root Node will have dist=0 and support=100
    (or 1.0), and the Node on the other side of root will inherit the
    dist which retains the dist information.

    Parameters
    ----------
    inplace: bool
        If True modify and return original tree, else return a copy.
    """
    tree = tree if inplace else tree.copy()
    inplace = bool(inplace)
    rootnode = tree.treenode

    # just return current tree if the rootnode node is not binary
    if len(rootnode.children) != 2:
        return tree

    # find a child with children, checking first left then right.
    if not rootnode.children[0].is_leaf():
        newroot = rootnode.children[0]
        ochild = rootnode.children[1]
    elif not rootnode.children[1].is_leaf():
        newroot = rootnode.children[1]
        ochild = rootnode.children[0]
    else:
        raise ToytreeError("Cannot unroot a tree with only two leaves")

    # child becomes ochild's new parent
    ochild._up = newroot
    newroot._children += (ochild,)

    # other child's dist extends to include child->oldrootnode dist
    ochild._dist += newroot.dist

    # ochild->child edge inherits features from child->oldrootnode edge
    ochild.support = newroot.support

    # make child the new rootnode and remove old rootnode
    newroot._up = None
    newroot.support = (
        100 if max(i.support for i in newroot.children) > 1 else 1.0)
    tree.treenode = newroot
    del rootnode

    # update idxs and return
    tree._update()
    return tree


if __name__ == "__main__":

    # Example test: start with a simple balanced tree.
    import toytree
    TREE = toytree.rtree.baltree(ntips=10)

    c, a, m = unroot(TREE).draw()
    _, a, m = root(TREE, 'r2')._draw_browser()

    # c2, a, m = unroot(TREE)._draw_browser(axes=a)
    # print(unroot(TREE))

    # unroot the tree
    # TREE = TREE.unroot()

    # root the tree a clade with the first two samples
    # TREE = TREE.root(['r1', 'r2'])

    # re-root on a different clade, for last two samples
    # TREE = TREE.root(['r9', 'r10'])

    # check that dist and support values were properly retained.
    # ...