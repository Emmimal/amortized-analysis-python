import pytest

from dynamic_array import DynamicArray


def test_items_keep_their_order() -> None:
    array = DynamicArray()
    for i in range(20):
        array.append(i)
    assert [array[i] for i in range(len(array))] == list(range(20))


def test_capacity_doubles_when_the_array_is_full() -> None:
    array = DynamicArray()
    capacities = []
    for i in range(9):
        array.append(i)
        capacities.append(array.capacity)
    assert capacities == [1, 2, 4, 4, 8, 8, 8, 8, 16]


def test_nine_appends_copy_fifteen_items() -> None:
    array = DynamicArray()
    for i in range(9):
        array.append(i)
    assert array.copies == 1 + 2 + 4 + 8


def test_index_out_of_range_raises() -> None:
    array = DynamicArray()
    array.append("a")
    with pytest.raises(IndexError):
        array[1]


def test_growth_function_must_increase_capacity() -> None:
    array = DynamicArray(grow=lambda capacity: capacity)
    array.append("a")
    with pytest.raises(ValueError):
        array.append("b")
