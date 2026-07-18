import unittest
import sys

sys.path.append("../")
from tree_node import TreeNode
from binary_tree import BinaryTree, BinTreeError


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.bt = BinaryTree()

        self.bt.put(TreeNode("b"))
        self.bt.put(TreeNode("c"))
        self.bt.put(TreeNode("a"))

    def test_put_rejects_non_tree_node(self):
        with self.assertRaises(BinTreeError):
            self.bt.put("a")

    def test_put_inserts_nodes_into_binary_search_tree_order(self):
        self.assertEqual(self.bt.root.key, "b")
        self.assertEqual(self.bt.root.left.key, "a")
        self.assertEqual(self.bt.root.right.key, "c")

    def test_exists_returns_true_for_existing_node(self):
        self.assertTrue(self.bt.exists(TreeNode("a", 1)))
        self.assertTrue(self.bt.exists(TreeNode("b", 2)))
        self.assertTrue(self.bt.exists(TreeNode("c", 3)))

    def test_exists_returns_false_for_missing_node(self):
        self.assertFalse(self.bt.exists(TreeNode("d")))

    def test_exists_rejects_non_tree_node(self):
        with self.assertRaises(BinTreeError):
            self.bt.exists("a")

if __name__ == "__main__":
    unittest.main()
