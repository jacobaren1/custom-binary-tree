# Custom Binary Tree

A small Python practice project focused on building a binary tree node class, introducing a simple `BinaryTree` structure, and exploring Python class behavior with custom comparison operators.

## Summary
This project is intended to reinforce core Python concepts such as:

- class design
- object attributes
- custom comparison methods
- recursive tree traversal and insertion
- unit testing with `unittest`

## Project Structure
```text
custom-binary-tree/
├── .github/
│   └── CODEOWNERS
├── binary_tree.py
├── tests/
│   ├── test_binary_tree.py
│   └── test_tree_node.py
├── .gitignore
├── .venv/                 # local virtual environment
├── readme.md
└── tree_node.py
```

## Usage
The main classes are `TreeNode` and `BinaryTree`.

```python
from tree_node import TreeNode
from binary_tree import BinaryTree

bt = BinaryTree()

bt.put(TreeNode("b"))
bt.put(TreeNode("a"))
bt.put(TreeNode("c"))

print(bt.exists(TreeNode("a")))
print(bt.exists(TreeNode("d")))
```

## Testing
Run the unit test suite from the project root with:

```bash
python -m unittest discover -s tests -v
```

## Notes

- `TreeNode` compares and orders nodes using its `key` field.
- `BinaryTree` currently supports inserting nodes and checking whether a node exists.
- The repository includes tests that validate both the comparison operators and the binary tree behavior.
