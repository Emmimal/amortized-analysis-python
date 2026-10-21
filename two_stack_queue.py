"""A first-in, first-out queue built from two stacks."""


class TwoStackQueue:
    """Queue that moves items between two lists only when it has to."""

    def __init__(self) -> None:
        self._inbox: list[object] = []
        self._outbox: list[object] = []
        self.moves = 0

    def __len__(self) -> int:
        return len(self._inbox) + len(self._outbox)

    def enqueue(self, item: object) -> None:
        """Add an item to the back of the queue."""
        self._inbox.append(item)

    def dequeue(self) -> object:
        """Remove and return the item at the front of the queue."""
        if not self._outbox:
            while self._inbox:
                self._outbox.append(self._inbox.pop())
                self.moves += 1
        if not self._outbox:
            raise IndexError("dequeue from empty queue")
        return self._outbox.pop()
