import unittest


class TestPackageImport(unittest.TestCase):
    def test_public_package_imports(self):
        from CustomBinaryTree import BinaryTree, TreeNode

        self.assertIsNotNone(BinaryTree)
        self.assertIsNotNone(TreeNode)


if __name__ == "__main__":
    unittest.main()
