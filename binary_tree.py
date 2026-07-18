from tree_node import TreeNode

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
    
    def put_func(self, node: TreeNode, ref_node: TreeNode | None):

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
