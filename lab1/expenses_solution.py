#!/usr/bin/env python3
"""
Personal Expense Tracker - Business Logic Module

Complete implementation of all functions marked with TODO.
Make sure to use proper type hints throughout your implementation.
"""

from dataclasses import dataclass
from functools import partial
from typing import Any, Optional

type TransactionList = list["Transaction"]
type Statistics = dict[str, Any]


@dataclass(frozen=True)
class Transaction:
    """
    Represents a single expense transaction.

    Fields should be as follows:
    - date: string in format YYYY-MM-DD
    - description: string description of the expense
    - category: string category (e.g., "Food", "Transport", "Entertainment")
    - amount: float amount in PLN
    """

    date: str
    description: str
    category: str
    amount: float


def add_transaction(
    transactions: TransactionList, transaction: Transaction
) -> TransactionList:
    """
    Add a new transaction to the transactions list.

    Args:
        transactions: Current list of transactions
        transaction: Transaction object to add

    Returns:
        Updated list of transactions
    """
    return transactions + [transaction]


def filter_by_category(transactions: TransactionList, category: str) -> TransactionList:
    """
    Filter transactions by category (case-insensitive).

    Args:
        transactions: List of transactions to filter
        category: Category name to filter by

    Returns:
        List of transactions matching the category
    """
    return [t for t in transactions if t.category.lower() == category.lower()]


def filter_by_amount_range(
    transactions: TransactionList, min_amount: float, max_amount: float
) -> TransactionList:
    """
    Filter transactions by amount range (inclusive).

    Args:
        transactions: List of transactions to filter
        min_amount: Minimum amount (inclusive)
        max_amount: Maximum amount (inclusive)

    Returns:
        List of transactions within the amount range
    """
    return [t for t in transactions if min_amount <= t.amount <= max_amount]


def calculate_statistics(transactions: TransactionList) -> Statistics:
    """
    Calculate and return expense statistics.

    Args:
        transactions: List of transactions to analyze

    Returns:
        Dictionary with statistics:
        - 'count': number of transactions
        - 'total': total amount spent
        - 'average': average amount per transaction
        - 'by_category': dict mapping category to total amount
    """
    count = len(transactions)
    total = sum(t.amount for t in transactions)
    average = total / count if count > 0 else 0.0
    by_category: dict[str, float] = {}
    for t in transactions:
        by_category[t.category] = by_category.get(t.category, 0.0) + t.amount
    return {
        'count': count,
        'total': total,
        'average': average,
        'by_category': by_category,
    }


# BONUS: Advanced Functions (Optional)


def create_category_filter(category: str):
    """
    Create a specialized filter function for a specific category using partial.

    Args:
        category: Category to create filter for

    Returns:
        Function that takes transactions list and returns filtered transactions

    Example usage:
        food_filter = create_category_filter("Food")
        food_transactions = food_filter(transactions)
    """
    return partial(filter_by_category, category=category)


def create_amount_filter(min_amount: float, max_amount: Optional[float] = None):
    """
    Create a specialized filter function for amount ranges using closures.

    Args:
        min_amount: Minimum amount
        max_amount: Maximum amount (if None, no upper limit)

    Returns:
        Function that takes transactions list and filters by amount

    Example usage:
        cheap_filter = create_amount_filter(0, 20)
        cheap_items = cheap_filter(transactions)
    """
    def _filter(transactions: TransactionList) -> TransactionList:
        if max_amount is None:
            return [t for t in transactions if t.amount >= min_amount]
        return [t for t in transactions if min_amount <= t.amount <= max_amount]
    return _filter


