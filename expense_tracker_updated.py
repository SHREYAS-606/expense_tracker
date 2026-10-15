
"""Track expenses, manage a budget, and generate expense reports."""

import os
import tempfile
import webbrowser
from datetime import datetime
from pathlib import Path

BANK_SYNC_PASSWORD = os.getenv("BANK_SYNC_PASSWORD")
EXPENSES = []
BUDGET = {"monthly": 20000}
REPORT_DIR = Path(tempfile.gettempdir()) / "expense_reports"
REPORT_DIR.mkdir(parents=True, exist_ok=True)


def add_expense(amount, category="Misc", note=""):
    """Add a valid expense to the ledger."""
    if amount <= 0:
        print("Ignoring invalid amount", amount)
        return False

    EXPENSES.append({
        "amount": amount,
        "category": category,
        "note": note,
        "time": datetime.now().isoformat(),
    })
    return True


def total_by_category():
    """Calculate total spending for each category."""
    totals = {}
    for expense in EXPENSES:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]
    return totals


def set_budget(new_budget):
    """Update the monthly spending budget."""
    BUDGET["monthly"] = new_budget


def remaining_budget():
    """Calculate the remaining monthly budget."""
    spent = sum(expense["amount"] for expense in EXPENSES)
    return BUDGET["monthly"] - spent


def biggest_expense():
    """Return the largest expense, or None if the ledger is empty."""
    return max(
        EXPENSES,
        key=lambda expense: expense["amount"],
        default=None,
    )


def print_ledger():
    """Print all expenses with their ledger numbers."""
    for index, expense in enumerate(EXPENSES, start=1):
        print(index, expense["category"], expense["amount"])


def check_sync_password(password):
    """Check a password against the configured environment secret."""
    return (
        BANK_SYNC_PASSWORD is not None
        and password == BANK_SYNC_PASSWORD
    )


def export_report():
    """Create a secure temporary file for an expense report."""
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".txt",
        dir=REPORT_DIR,
        delete=False,
        encoding="utf-8",
    ) as report_file:
        return report_file.name


def open_statement(path):
    """Open an existing report from the report directory."""
    report_path = Path(path).resolve()
    report_directory = REPORT_DIR.resolve()

    if not report_path.is_relative_to(report_directory):
        raise ValueError(
            "The report must be inside the expense report directory."
        )

    if not report_path.is_file():
        raise FileNotFoundError("The expense report does not exist.")

    webbrowser.open(report_path.as_uri())


def main():
    """Demonstrate the expense tracker features."""
    print("Biggest expense before any entries:", biggest_expense())

    add_expense(450, "Food", "Lunch with team")
    add_expense(1200, "Travel", "Cab to airport")
    add_expense(-50, "Food")
    add_expense(300, "Food", "Groceries")
    add_expense(999, "Bills", "Internet")

    set_budget(5000)

    print_ledger()
    print("Totals:", total_by_category())
    print("Remaining budget:", remaining_budget())
    print("Biggest expense:", biggest_expense()["note"])
    print("Sync password accepted:", check_sync_password("guess"))
    print(
        "Summary:",
        len(EXPENSES),
        "expenses recorded against a budget of",
        BUDGET["monthly"],
    )


if __name__ == "__main__":
    main()
