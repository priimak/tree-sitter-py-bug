from pathlib import Path

import tree_sitter_python
from tree_sitter import Language, Node, Parser, Query, QueryCursor

PY_LANGUAGE = Language(tree_sitter_python.language())
PYTHON_PARSER = Parser(PY_LANGUAGE)
HIGHLIGHTER_QUERY = Query(
    PY_LANGUAGE,
    """
        (call (identifier) @function_call)
    """,
)

if __name__ == "__main__":
    text = (Path(__file__).parent.parent.parent / "app_py.txt").read_text()
    input_text = text.encode()
    tree = PYTHON_PARSER.parse(input_text)
    query_cursor = QueryCursor(HIGHLIGHTER_QUERY)

    matches: list[tuple[int, dict[str, list[Node]]]] = query_cursor.matches(
        tree.root_node
    )
    matches.sort(key=lambda m: m[0])
    for _, m in matches:
        for capture_name, nodes in m.items():
            for node in nodes:
                txt = node.text.decode()
                if txt == "foobar":
                    print(
                        f"{txt} :: {node.start_point}: row={node.start_point.row}, column={node.start_point.column}"
                    )
