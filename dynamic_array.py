"""A dynamic array that counts how many items it copies."""

from collections.abc import Callable


def double(capacity: int) -> int:
    """Grow geometrically: the new capacity is twice the old one."""
    return capacity * 2


class DynamicArray:
    """A growable array backed by a fixed-size Python list.

    The array starts with room for one item. When it is full, it asks
    ``grow`` for a bigger capacity, allocates a new block, and copies every
    item across. Each copy is counted in ``copies``.
    """

    def __init__(self, grow: Callable[[int], int] = double) -> None:
        self._grow = grow
        self._capacity = 1
        self._size = 0
        self._slots: list[object] = [None] * self._capacity
        self.copies = 0

    @property
    def capacity(self) -> int:
        """Return how many items fit before the next resize."""
        return self._capacity

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int) -> object:
        if not 0 <= index < self._size:
            raise IndexError("index out of range")
        return self._slots[index]

    def append(self, value: object) -> None:
        """Add a value at the end, resizing first if the array is full."""
        if self._size == self._capacity:
            self._resize(self._grow(self._capacity))
        self._slots[self._size] = value
        self._size += 1

    def _resize(self, new_capacity: int) -> None:
        if new_capacity <= self._capacity:
            raise ValueError("new capacity must be larger than the old one")
        new_slots: list[object] = [None] * new_capacity
        for i in range(self._size):
            new_slots[i] = self._slots[i]
            self.copies += 1
        self._slots = new_slots
        self._capacity = new_capacity
