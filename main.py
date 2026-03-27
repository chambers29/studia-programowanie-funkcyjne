#!/usr/bin/env python3
"""
Personal Expense Tracker - Test Client
"""

import traceback

from expenses_solution import (
    Transaction,
    TransactionList,
    add_transaction,
    calculate_statistics,
    filter_by_amount_range,
    filter_by_category,
)


def test_basic_functionality() -> list:
    """Test basic add and display functionality."""
    print("=== Testing Basic Functionality ===")

    # Start with empty list
    transactions: TransactionList = []

    # Add some test transactions
    for t in [
        Transaction("2024-10-15", "Coffee", "Food", 12.50),
        Transaction("2024-10-16", "Bus ticket", "Transport", 3.50),
        Transaction("2024-10-17", "Movie", "Entertainment", 25.00),
        Transaction("2024-10-19", "Burger", "Food", 30.00),
        Transaction("2024-10-20", "Fuel", "Transport", 200.00),
        Transaction("2024-10-21", "Bus ticket", "Transport", 3.50),
    ]:
        transactions = add_transaction(transactions, t)

    print(f"Added {len(transactions)} transactions:")

    for t in transactions:
        print(f"  {t.date} | {t.category} | {t.description} | {t.amount:.2f} PLN")

    print()
    return transactions


def test_filtering(transactions: list) -> None:
    """Test filtering functions."""
    print("=== Testing Filtering ===")

    # Filter by category
    food_expenses = filter_by_category(transactions, "Food")
    print(f"Food expenses ({len(food_expenses)} found):")
    assert len(food_expenses) == 2
    for t in food_expenses:
        print(f"  {t.description}: {t.amount:.2f} PLN")

    # Filter by amount range
    cheap_items = filter_by_amount_range(transactions, 0.0, 15.0)
    print(f"\nCheap items (0-15 PLN, {len(cheap_items)} found):")
    assert len(cheap_items) == 3
    for t in cheap_items:
        print(f"  {t.description}: {t.amount:.2f} PLN")

    print()


def test_statistics(transactions: list) -> None:
    """Test statistics calculation."""
    print("=== Testing Statistics ===")

    stats = calculate_statistics(transactions)

    # These fields should be defined in the stats:
    assert "count" in stats
    assert "total" in stats
    assert "average" in stats
    assert "by_category" in stats

    print(f"Total transactions: {stats['count']}")
    print(f"Total amount: {stats['total']:.2f} PLN")
    print(f"Average amount: {stats['average']:.2f} PLN")

    print("By category:")
    for category, amount in stats["by_category"].items():
        print(f"  {category}: {amount:.2f} PLN")

    print()


def main() -> None:
    """Run all tests."""
    print("Personal Expense Tracker - Testing Functions")
    print()

    try:
        # Test basic functionality and get transactions
        transactions = test_basic_functionality()

        # Test other functions with transactions
        test_filtering(transactions)
        test_statistics(transactions)

        print("All tests completed!")
    except NotImplementedError as e:
        print(f"Function not implemented yet: {e}")
        traceback.print_exc()
    except AssertionError as e:
        print(f"One of test asserts failed: {e}")
        traceback.print_exc()
    except Exception as e:
        print(f"Error during testing: {e}")
        print("Check your implementation in expenses.py")
        traceback.print_exc()


if __name__ == "__main__":
    main()
