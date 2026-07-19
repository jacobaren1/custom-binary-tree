# Custom Binary Tree

A small Python package that provides a simple binary search tree implementation using `TreeNode` and `BinaryTree`.

## Overview
This project is designed as a lightweight practice repository for learning:

- class design in Python
- custom comparison methods
- recursive tree insertion and lookup
- unit testing with `unittest`
- packaging Python modules for import via a public namespace

## Installation
Install the package from the repository root in editable mode:

```bash
python -m pip install -e .
```

## Quickstart
After installation, you can import the package with:

```python
from CustomBinaryTree import BinaryTree, TreeNode

bt = BinaryTree()

bt.put(TreeNode("b"))
bt.put(TreeNode("a"))
bt.put(TreeNode("c"))

print(bt.exists(TreeNode("a")))
print(bt.exists(TreeNode("d")))
```

## Package API
The public package exports:

- `BinaryTree`
- `TreeNode`
- `BinTreeError`

## Project Structure
```text
custom-binary-tree/
├── CustomBinaryTree/
│   ├── __init__.py
│   ├── binary_tree.py
│   └── tree_node.py
├── tests/
│   ├── test_binary_tree.py
│   ├── test_tree_node.py
│   └── test_package_import.py
├── pyproject.toml
├── readme.md
└── requirements.txt
```

## Testing
Run the full unit test suite from the project root:

```bash
python -m unittest discover -s tests -v
```

## Notes

- `TreeNode` orders and compares nodes using the `key` field.
- `BinaryTree` supports node insertion and membership checks.
- The package is intentionally minimal and focused on clear, readable Python behavior.
