A Bug?
======

```shell
git clone https://github.com/priimak/tree-sitter-py-bug.git
cd tree-sitter-py-bug/
uv sync
uv run src/tree_sitter_py_bug/main.py 
```

```shell
foobar :: <Point row=256, column=8>: row=256, column=8
foobar :: <Point row=258, column=12>: row=0, column=12
```

In the second row you will see that in `Point.__repr__` it reports row 258 while `point.row` return value 0.