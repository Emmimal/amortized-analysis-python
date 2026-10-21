import pytest

from two_stack_queue import TwoStackQueue


def test_items_come_out_in_first_in_first_out_order() -> None:
    queue = TwoStackQueue()
    for i in range(1, 6):
        queue.enqueue(i)
    assert [queue.dequeue() for _ in range(3)] == [1, 2, 3]
    queue.enqueue(6)
    assert [queue.dequeue() for _ in range(3)] == [4, 5, 6]


def test_dequeue_from_an_empty_queue_raises() -> None:
    with pytest.raises(IndexError):
        TwoStackQueue().dequeue()


def test_each_item_moves_at_most_once() -> None:
    queue = TwoStackQueue()
    for i in range(1_000):
        queue.enqueue(i)
    for _ in range(500):
        queue.dequeue()
    for i in range(1_000, 1_500):
        queue.enqueue(i)
    while len(queue):
        queue.dequeue()
    assert queue.moves <= 1_500
