#pre commit checks?

# pre-commit run --all
black....................................................................Passed
trim trailing whitespace.................................................Passed
fix end of files.........................................................Passed
fix requirements.txt.....................................................Passed
check python ast.........................................................Failed
- hook id: check-ast
- exit code: 1

examples/adaptive-crag/application.py: failed parsing with CPython 3.10.12:

    Traceback (most recent call last):
      File "/home/nduta/.cache/pre-commit/reporbt9swuh/py_env-python3/lib/python3.10/site-packages/pre_commit_hooks/check_ast.py", line 21, in main
        ast.parse(f.read(), filename=filename)
      File "/usr/lib/python3.10/ast.py", line 50, in parse
        return compile(source, filename, mode, flags,
      File "examples/adaptive-crag/application.py", line 268
        routes = Literal[*table_names, "web_search", "assistant"]  # type: ignore
                         ^
    SyntaxError: invalid syntax

isort....................................................................Passed
flake8...................................................................Failed
- hook id: flake8
- exit code: 1

examples/adaptive-crag/application.py:268:23: E999 SyntaxError: invalid syntax

frontend-lint-staged.....................................................Failed
- hook id: frontend-lint-staged
- exit code: 1

file:///home/nduta/.npm/_npx/8facc973fbdb1091/node_modules/lint-staged/bin/lint-staged.js:23
const packageJson = JSON.parse(await fs.readFile(new URL('../package.json', import.meta.url)))
                               ^^^^^

SyntaxError: Unexpected reserved word
    at Loader.moduleStrategy (internal/modules/esm/translators.js:133:18)
    at async link (internal/modules/esm/module_job.js:42:21)
