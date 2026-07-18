

class TreeNode(object):

    def __init__(self, key: ..., value:... = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"TreeNode: {self.key}: {self.value}"


if __name__ == "__main__":

    my_node = TreeNode("hej")
    print(my_node)
