"""Helpers that turn a DynamicArray's work into numbers you can check."""

from collections.abc import Callable

from dynamic_array import DynamicArray, double


def append_costs(n: int, grow: Callable[[int], int] = double) -> list[int]:
    """Return the cost of each of n appends: one write plus items copied."""
    array = DynamicArray(grow)
    costs: list[int] = []
    for i in range(n):
        copies_before = array.copies
        array.append(i)
        costs.append(1 + array.copies - copies_before)
    return costs


def bank_balances(costs: list[int], charge: int) -> list[int]:
    """Return the bank balance after each operation (accounting method)."""
    balance = 0
    balances: list[int] = []
    for cost in costs:
        balance += charge - cost
        balances.append(balance)
    return balances


def potential(size: int, capacity: int) -> int:
    """Return the potential function used for the dynamic array."""
    return 2 * size - capacity


def amortized_costs(n: int) -> list[int]:
    """Return actual cost + change in potential for each of n appends."""
    array = DynamicArray()
    result: list[int] = []
    for i in range(n):
        potential_before = potential(len(array), array.capacity)
        copies_before = array.copies
        array.append(i)
        actual = 1 + array.copies - copies_before
        potential_after = potential(len(array), array.capacity)
        result.append(actual + potential_after - potential_before)
    return result
