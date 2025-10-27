# Issue Summary - Lab 5

| Issue Type | Tool | Line(s) | Description | Fix Applied |
|-------------|------|----------|--------------|--------------|
| Dangerous default argument | Pylint | 8 | Used mutable list `[]` as default parameter | Changed to `None` and initialized inside function |
| Bare except | Bandit / Pylint | 19 | `except:` caught all errors | Replaced with `except KeyError as e:` |
| File handling issue | Pylint | 26, 32 | `open()` used without encoding or context manager | Replaced with `with open(..., encoding='utf-8'):` |
| Use of eval() | Bandit | 59 | Insecure function call | Removed `eval()` and replaced with safe code |
| Naming & formatting | Pylint / Flake8 | Various | Function names not in `snake_case`, missing docstrings | Renamed functions, added docstrings, and formatted correctly |
