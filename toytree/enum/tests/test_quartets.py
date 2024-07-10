
"""Test enumeration methods to find partitions in a tree.

- iter_bipartitions
- iter_quartets
"""


import unittest
import toytree
# from toytree.utils import ToytreeError
from toytree.enum import _iter_unresolved_quartet_sets, _iter_quartet_sets, iter_quartets


class TestQuartets(unittest.TestCase):
    def setUp(self):
        """Six tip tree three clades of two."""
        self.tree1 = toytree.tree("(a,b,((c,d)CD,(e,f)EF)X)AB;")
        self.tree2 = self.tree1.root("a")
        self.tree3 = self.tree1.root("a", "b")
        self.trees = [self.tree1, self.tree2, self.tree3]
    def test_iter_quatet_sets(self):
        PARTS = [('c', 'f', 'b', 'a'),
                ('d', 'c', 'a', 'f'),
                ('d', 'c', 'b', 'a'),
                ('d', 'c', 'b', 'f'),
                ('d', 'c', 'e', 'a'),
                ('d', 'c', 'e', 'b'),
                ('d', 'c', 'e', 'f'),
                ('d', 'f', 'b', 'a'),
                ('e', 'c', 'b', 'a'),
                ('e', 'd', 'b', 'a'),
                ('e', 'f', 'b', 'a'),
                ('e', 'f', 'b', 'c'),
                ('e', 'f', 'b', 'd'),
                ('e', 'f', 'c', 'a'),
                ('e', 'f', 'd', 'a')]
        BIPARTITION_PARTS = [('c', 'd', 'e', 'a'),
                ('c', 'd', 'e', 'b'),
                ('c', 'd', 'f', 'a'),
                ('c', 'd', 'f', 'b'),
                ('c', 'e', 'a', 'b'),
                ('c', 'f', 'a', 'b'),
                ('d', 'e', 'a', 'b'),
                ('d', 'f', 'a', 'b'),
                ('e', 'f', 'c', 'a'),
                ('e', 'f', 'c', 'b'),
                ('e', 'f', 'd', 'a'),
                ('e', 'f', 'd', 'b')]
        parts = sorted(_iter_quartet_sets(self.tree1, feature = 'name'))
        bipartition_parts = sorted(_iter_quartet_sets(self.tree1, feature = 'name', quadripartitions = True))
        self.assertEqual(parts, PARTS)
        self.assertEqual(bipartition_parts, BIPARTITION_PARTS)
    def test_iter_unresolved_quartet_sets(self):
        PARTS = [{'a', 'b', 'c', 'd'},
                {'a', 'b', 'c', 'e'},
                {'a', 'b', 'c', 'f'},
                {'a', 'b', 'd', 'e'},
                {'a', 'b', 'd', 'f'},
                {'a', 'b', 'e', 'f'},
                {'a', 'c', 'd', 'e'},
                {'a', 'c', 'd', 'f'},
                {'a', 'c', 'e', 'f'},
                {'a', 'd', 'e', 'f'},
                {'b', 'c', 'd', 'e'},
                {'b', 'c', 'd', 'f'},
                {'b', 'c', 'e', 'f'},
                {'b', 'd', 'e', 'f'},
                {'c', 'd', 'e', 'f'}]
        parts = list(_iter_unresolved_quartet_sets(self.tree1, feature = 'name'))
        self.assertEqual(parts, PARTS)
    def test_iter_quartets(self):
        """Quartets"""
        PARTS = [({'c', 'd'}, {'e', 'f'}),
                ({'c', 'd'}, {'b', 'e'}),
                ({'c', 'd'}, {'a', 'e'}),
                ({'c', 'd'}, {'b', 'f'}),
                ({'c', 'd'}, {'a', 'f'}),
                ({'c', 'd'}, {'a', 'b'}),
                ({'e', 'f'}, {'b', 'd'}),
                ({'e', 'f'}, {'a', 'd'}),
                ({'e', 'f'}, {'b', 'c'}),
                ({'e', 'f'}, {'a', 'c'}),
                ({'e', 'f'}, {'a', 'b'}),
                ({'d', 'e'}, {'a', 'b'}),
                ({'d', 'f'}, {'a', 'b'}),
                ({'c', 'e'}, {'a', 'b'}),
                ({'c', 'f'}, {'a', 'b'})]
        parts = sorted(iter_quartets(self.tree1, ))
        self.assertEqual(parts, PARTS)

        




if __name__ == "__main__":

    unittest.main()
