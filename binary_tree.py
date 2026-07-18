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
        
        self.put_func(node)
    
    def put_func(self, node):
        pass
