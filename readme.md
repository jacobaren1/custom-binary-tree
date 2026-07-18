# Custom Binary Tree

A small Python practice project focused on building a binary tree node class and exploring Python class behavior, including custom comparison operators.

## Summary
This project is intended to reinforce core Python concepts such as:

- class design
- object attributes
- custom comparison methods
- unit testing with `unittest`

## Project Structure
```text
custom-binary-tree/
├── .github/
│   └── CODEOWNERS
├── tests/
│   └── test_tree_node.py
├── .gitignore
├── .venv/                 # local virtual environment
├── readme.md
└── tree_node.py
```

## Usage
The main class is `TreeNode`, which stores a `key`, an optional `value`, and child references for a binary tree.

```python
from tree_node import TreeNode

root = TreeNode("hej", 1)
left = TreeNode("abc", 2)
right = TreeNode("xyz", 3)

root.left = left
root.right = right

print(root)
```

## Testing
Run the unit test suite from the project root with:

```bash
python -m unittest discover -s tests -v
```

## Notes

- The project currently uses a simple `TreeNode` implementation with custom ordering behavior based on the `key` field.
- The repository includes a small test suite to validate the comparison operators.
