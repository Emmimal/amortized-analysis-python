"""Measure the cost of appends and compare growth strategies."""

import sys

from analysis import append_costs
from dynamic_array import DynamicArray, double


def add_ten(capacity: int) -> int:
    """Grow by a fixed amount instead of by a factor."""
    return capacity + 10


def show_cost_per_append() -> None:
    print("Cost per append for a doubling array")
    for n in (10, 100, 1_000, 100_000):
        array = DynamicArray()
        for i in range(n):
            array.append(i)
        total_cost = n + array.copies
        print(f"n={n:>7,}  total cost={total_cost:>9,}  per append={total_cost / n:.2f}")


def show_first_costs() -> None:
    print("\nCost of each of the first 17 appends")
    print(append_costs(17))


def show_cpython_growth() -> None:
    print("\nHow CPython's list grows")
    items: list[int] = []
    last_size = sys.getsizeof(items)
    print(f"len= 0 -> {last_size} bytes")
    for i in range(1, 65):
        items.append(i)
        size = sys.getsizeof(items)
        if size != last_size:
            print(f"len={i:>2} -> {size} bytes")
            last_size = size


def show_growth_strategies() -> None:
    print("\nItems copied: doubling vs adding 10 slots")
    for n in (1_000, 10_000, 100_000):
        doubling = DynamicArray(double)
        fixed = DynamicArray(add_ten)
        for i in range(n):
            doubling.append(i)
            fixed.append(i)
        print(f"n={n:>7,}  doubling={doubling.copies:>9,}  add 10={fixed.copies:>12,}")


if __name__ == "__main__":
    show_cost_per_append()
    show_first_costs()
    show_cpython_growth()
    show_growth_strategies()
