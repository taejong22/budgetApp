"""Core business logic for the budget app."""

from __future__ import annotations

from pathlib import Path
from typing import TypedDict


class Transaction(TypedDict):
    """A single budget transaction."""

    date: str
    type: str
    category: str
    description: str
    amount: int
    memo: str


def add_transaction(
    transactions: list[Transaction],
    transaction: Transaction,
) -> list[Transaction]:
    """Add a transaction to the transaction list and return the updated list."""
    return [*transactions, dict(transaction)]


def get_balance(transactions: list[Transaction]) -> float:
    """Return the sum of all transaction amounts."""
    return float(sum(transaction["amount"] for transaction in transactions))


def filter_by_category(transactions: list[Transaction], category: str) -> list[Transaction]:
    """Return transactions that match the given category."""
    pass


def load_transactions_from_csv(csv_path: Path) -> list[Transaction]:
    """Load transactions from a CSV file."""
    pass


def monthly_summary(transactions: list[Transaction]) -> dict[str, dict[str, int]]:
    """Summarize transactions by month."""
    pass
