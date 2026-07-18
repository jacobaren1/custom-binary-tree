# --- Standard modules ---
import unittest
import sys

# --- Import from parent dir ---
sys.path.append("../")
from tree_node import TreeNode

class TestTreeNodeComparisonOperators(unittest.TestCase):
    def test_eq_compares_only_the_key_field(self):
        left = TreeNode("a", 1)
        right = TreeNode("a", 2)

        self.assertEqual(left, right)

    def test_eq_returns_false_for_nodes_with_different_keys(self):
        left = TreeNode("a", 1)
        right = TreeNode("b", 2)

        self.assertNotEqual(left, right)

    def test_lt_returns_true_when_left_key_is_smaller(self):
        left = TreeNode("a", 1)
        right = TreeNode("b", 2)

        self.assertLess(left, right)

    def test_gt_returns_true_when_left_key_is_larger(self):
        left = TreeNode("z", 1)
        right = TreeNode("a", 2)

        self.assertGreater(left, right)

    def test_lt_and_gt_are_false_for_equal_keys(self):
        left = TreeNode("same", 1)
        right = TreeNode("same", 2)

        self.assertFalse(left < right)
        self.assertFalse(left > right)


if __name__ == "__main__":
    unittest.main()
