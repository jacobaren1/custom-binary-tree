import unittest

class TreeNode(object):

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
