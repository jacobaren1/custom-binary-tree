import unittest
import sys

sys.path.append("../")
from tree_node import TreeNode
from binary_tree import BinaryTree, BinTreeError


class TestBinaryTreePut(unittest.TestCase):
    bt = BinaryTree()
    
    def test_put_rejects_non_tree_node(self):
        with self.assertRaises(BinTreeError):
            self.bt.put("a")

    def test_put_accepts_tree_node(self):
        bt.put( TreeNode("a") )
        self.assertIsNotNone(bt.root)

if __name__ == "__main__":
    unittest.main()
