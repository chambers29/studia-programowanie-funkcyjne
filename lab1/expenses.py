#!/usr/bin/env python3
"""
Personal Expense Tracker - Business Logic Module

Complete implementation of all functions marked with TODO.
Make sure to use proper type hints throughout your implementation.
"""

from dataclasses import dataclass
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

    # TODO: Add fields with proper type hints
    pass


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
    # TODO: Add transaction to the list and return updated list
    raise NotImplementedError


def filter_by_category(transactions: TransactionList, category: str) -> TransactionList:
    """
    Filter transactions by category (case-insensitive).

    Args:
        transactions: List of transactions to filter
        category: Category name to filter by

    Returns:
        List of transactions matching the category
    """
    # TODO: Filter transactions by category
    # HINT: Use list comprehension and .lower() for case-insensitive comparison
    raise NotImplementedError


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
    # TODO: Filter transactions by amount range
    # HINT: Use list comprehension with range conditions
    raise NotImplementedError


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
    # TODO: Calculate statistics
    # HINT: Use sum(), len(), and dictionary comprehension or loop for categories

    # Example return structure:
    # return {
    #     'count': 0,
    #     'total': 0.0,
    #     'average': 0.0,
    #     'by_category': {}
    # }
    raise NotImplementedError


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
    # TODO (BONUS): Implement using partial application
    # HINT: Use functools.partial with filter_by_category
    pass


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
    # TODO (BONUS): Implement using nested functions (closures)
    pass


# Example usage and testing
if __name__ == "__main__":
    # TODO (OPTIONAL): Add test code here to verify your functions work
    # Example test:
    # transactions = []
    # sample_transaction = Transaction("2023-10-15", "Coffee", "Food", 12.50)
    # transactions = add_transaction(transactions, sample_transaction)
    # print(f"Total transactions: {len(get_all_transactions(transactions))}")
    pass
