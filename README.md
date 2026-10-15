# Lab 5: Static Code Analysis — Personal Expense Tracker

## About the Project

This project demonstrates static code analysis using **Pylint, Bandit, and Flake8** on a Python-based Personal Expense Tracker.

The program records expenses by category, validates expense amounts, calculates category-wise totals, tracks the remaining budget, identifies the biggest expense, and checks a bank-sync password.

## Tools Used

- **Pylint** — Identifies code quality issues, naming problems, missing docstrings, and other potential improvements.
- **Bandit** — Detects common security issues in Python code.
- **Flake8** — Checks Python code for style violations and formatting problems.

## Work Completed

1. Ran the original expense tracker and recorded its output.
2. Executed Pylint, Bandit, and Flake8 to identify code quality, security, and style issues.
3. Documented the identified issues and their proposed fixes.
4. Updated the code to address the identified issues.
5. Ran all three tools again to verify the improvements.
6. Checked that the expense tracker continued to run successfully after the changes.

## Issues Addressed

- Replaced the hardcoded bank-sync password with an environment variable.
- Replaced insecure temporary-file creation with `tempfile.NamedTemporaryFile`.
- Removed unsafe shell-command execution and used Python's `webbrowser` module instead.
- Added input validation to reject invalid expense amounts.
- Improved naming conventions, documentation, and code organization.
- Corrected formatting and whitespace issues reported by Flake8.

## Project Structure

```text
L5_32_expense_tracker/
├── expense_tracker.py
├── issues.md
├── reflection.md
├── pylint_report.txt
├── bandit_report.txt
├── flake8_report.txt
└── README.md
```

The report files contain the initial analysis results. The final analysis results should also be included so that the improvements can be compared before and after the fixes.

## How to Run

Install the required tools:

```bash
python -m pip install pylint bandit flake8
```

Run the expense tracker:

```bash
python expense_tracker.py
```

Run static analysis:

```bash
python -m pylint expense_tracker.py
python -m bandit -r expense_tracker.py
python -m flake8 expense_tracker.py
```

## Verification

The cleaned implementation was tested to confirm that it runs successfully and preserves the main expense-tracking functionality.

The updated file achieved a **Pylint score of 10.00/10**, and Bandit reported no issues. Flake8 completed without reporting violations.

## Deliverables

- `expense_tracker.py` — Cleaned source code.
- `issues.md` — Documented issues, severity, descriptions, and fixes.
- `reflection.md` — Answers to the lab reflection questions.
- Pylint, Bandit, and Flake8 reports — Before-and-after analysis results.

## Git Commit History

The work was recorded in three commits:

- `Fix Pylint code quality issues`
- `Document Bandit security analysis`
- `Document Flake8 style analysis`

