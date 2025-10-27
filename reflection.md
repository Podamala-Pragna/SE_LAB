# Reflection - Lab 5: Static Code Analysis

### 1. Which issues were the easiest and hardest to fix?
- **Easiest:** Formatting issues (missing blank lines, naming conventions) — easily fixed using Pylint and Flake8 suggestions.
- **Hardest:** Replacing `eval()` and fixing the file handling with context managers — needed careful changes to avoid breaking functionality.

### 2. Did the tools report any false positives?
- No false positives. Every issue identified by Pylint, Flake8, and Bandit helped improve my code’s quality and security.

### 3. How would you integrate static analysis into a real project?
- I would integrate **Pylint**, **Flake8**, and **Bandit** in a **Continuous Integration (CI)** workflow.
- They can run automatically before merging pull requests.
- Developers can also use **pre-commit hooks** to ensure clean code before committing.

### 4. What improvements did you observe after fixing the issues?
- The code is now clean, readable, and secure.
- Achieved a **Pylint score of 9.57/10**.
- Removed unsafe `eval()` and replaced it with a secure method.
- No Bandit security warnings remain.
- Code follows PEP 8 conventions.
