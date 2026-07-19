from typing import Optional

from .tree_node import TreeNode


class BinTreeError(Exception):
    pass


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def put(self, node: TreeNode):

        if not isinstance(node, TreeNode):
            raise BinTreeError(
                f"A node in a binary tree must be a TreeNode, got {type(node)}"
            )

        self.root = self.put_func(node, self.root)

    def put_func(self, node: TreeNode, ref_node: Optional[TreeNode]) -> TreeNode:

        if ref_node is None:
            ref_node = node
            return ref_node

        elif node < ref_node:

            ref_node.left = self.put_func(node, ref_node.left)
            return ref_node

        elif node > ref_node:
            ref_node.right = self.put_func(node, ref_node.right)
            return ref_node

        else:
            print("Node already exists:", ref_node)
            return ref_node

    def exists(self, node: TreeNode):

        if not isinstance(node, TreeNode):
            raise BinTreeError(
                f".exists() must take TreeNode as input, got {type(node)}"
            )

        return self.exists_func(node, self.root)

    def exists_func(self, node: TreeNode, ref_node: Optional[TreeNode]) -> bool:

        if ref_node is None:
            return False

        elif node == ref_node:
            return True

        elif node < ref_node:
            return self.exists_func(node, ref_node.left)

        elif node > ref_node:
            return self.exists_func(node, ref_node.right)
