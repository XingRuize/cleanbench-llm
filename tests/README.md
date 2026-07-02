# Test organization

The `tests` directory mirrors the package structure under `src/cleanbench`.
Each source module has one corresponding test module instead of creating one
file for every function.

```text
src/cleanbench/                  tests/
├── corruption/                 ├── corruption/
│   ├── formatting.py           │   ├── test_formatting.py
│   ├── semantic.py             │   ├── test_semantic.py
│   └── pipeline.py             │   └── test_pipeline.py
├── cleaners/                   ├── cleaners/
├── evaluation/                 ├── evaluation/
├── experiments/                ├── experiments/
├── io/                         ├── io/
├── reporting/                  ├── reporting/
└── schemas/                    └── schemas/
```

Test functions should describe the behavior and the component under test, for
example `test_whitespace_can_apply` and `test_whitespace_corrupt_is_reproducible`.

Run all tests from the project root:

```powershell
python -m pytest -v
```

Run only formatting corruptor tests:

```powershell
python -m pytest tests\corruption\test_formatting.py -v
```
