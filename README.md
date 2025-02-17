Toytree
==========

Tree plotting with **Toytree** in Python
----------------------------------------
Welcome to toytree, a Python library for tree visualization, manipulation,
and numerical and evolutionary analyses. If you are new to toytree, head to 
the [User Guide](https://eaton-lab.org/toytree/quick_guide/) to see 
examples and learn about its features.

Toytree builds upon the Node data structure from the [ete3](http://etetoolkit.org/docs/latest/tutorial/tutorial_trees.html) library, but aims to provide
a more user-friendly object-oriented framework for interactive coding 
through our ToyTree object. The toytree library includes a suite of 
growing and extendable modules for analyses of trees and of data on trees.
It also includes modern plotting tools built on the [toyplot](http://toyplot.rtfd.io/) 
plotting library. The goal of toytree is to provide a light-weight Python equivalent to commonly used tree manipulation and plotting libraries in R, 
and in doing so, to promote further development of phylogenetic methods in Python. Toytree generates rich interactive figures (SVG+HTML+JS) that can be embedded in jupyter-notebooks or webpages, or rendered in SVG, PDF, or PNG for publications. 
The library is small and easy to install, making it easy to incorporate into 
other projects. 


Current release info
--------------------
| Name | Downloads | Version | Platforms |
| --- | --- | --- | --- |
| [![Conda Recipe](https://img.shields.io/badge/recipe-toytree-green.svg)](https://anaconda.org/conda-forge/toytree) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/toytree.svg)](https://anaconda.org/conda-forge/toytree) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/toytree.svg)](https://anaconda.org/conda-forge/toytree) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/toytree.svg)](https://anaconda.org/conda-forge/toytree) |

Installing toytree
-------------------
Toytree can be installed using conda or pip (conda preferred):
```
conda install toytree -c conda-forge
```
It is possible to list all of the versions of `toytree` available on your platform with:
```
conda search toytree --channel conda-forge
```

Documentation
-------------
See the [full documentation](http://eaton-lab.org/toytree) to learn more about plotting options, analysis methods, and other features of toytree. You can try out toytree in the cloud before installing by visiting the [toytree binder](http://mybinder.org/repo/eaton-lab/toytree).


Example code
------------

```python
# import toyplot and load a newick file from a public URL
import toytree
tre = toytree.tree("https://eaton-lab.org/data/Cyathophora.tre")

# root the tree using a wildcard string matching and draw a tree figure.
rtre = tre.root('~prz')
rtre.draw(width=400, tip_labels_align=True);

# or chain a few functions together
tre.root('~prz').drop_tips("~tham").ladderize().draw();

# extensive styling options are available
rtre.draw(
    tip_labels_colors='pink',
    node_labels='support',
    node_sizes=15,
    node_colors="cyan",
    edge_style={
        "stroke": "darkgrey", 
        "stroke-width": 3,
    },
)
```

Example plots
------------

![./manuscript/ToyTree-figure.svg](./manuscripts/toytree-1.0/ToyTree-figure.svg)
