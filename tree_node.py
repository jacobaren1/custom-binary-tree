import unittest

class TreeNode(object):
    """
    Represents a node in a binary tree.

    Parameters
    ----------
    key : Any
        The comparison key used to order the node in the tree.
    value : Any, optional
        The stored value associated with the node.

    Attributes
    ----------
    key : Any
        The node's ordering key.
    value : Any, optional
        The value stored in the node.
    left : TreeNode or None
        Reference to the left child node.
    right : TreeNode or None
        Reference to the right child node.
    """

    def __init__(self, key: ..., value:... = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"TreeNode: {self.key}: {self.value}"

    def __lt__(self, other):
        return self.key < other.key

    def __eq__(self, other):
        return self.key == other.key

    def __gt__(self, other):
        return self.key > other.key
