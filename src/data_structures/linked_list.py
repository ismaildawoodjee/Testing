class Node:
    def __init__(self, data=None, next_=None):
        """Node object to hold data.

        Args:
            data (any, optional): data in the node. Defaults to None.
            next_ (Node, optional): pointer to next node. Defaults to None.
        """
        self.data = data
        self.next_: Node = next_

    def __repr__(self) -> str:
        """String representation of Node. More general than __str__."""
        if self.data is not None:
            return f"[{self.data}]"

        return "[]"


class LinkedList:
    def __init__(self, head=None):
        """LinkedList object. Any linked list can be referenced from its head.

        Args:
            head (Node, optional): linked list's head node. Defaults to None.
        """
        self.head: Node | None = head

    def add(self, value) -> Node:
        """Add a new node containing data at the end of the linked list.

        Args:
            value (any): data for the new node

        Returns:
            tail (Node): final node in the linked list
        """
        if self.head is not None:
            current = self.head
            while current.next_:
                current = current.next_
            current.next_ = Node(value)
            return current.next_

        self.head = Node(value)
        return self.head

    def add_to_beginning(self, value) -> Node:
        """Add new node to the beginning of the linked list.

        Args:
            value (data): data for the new node

        Returns:
            head (Node): first node in the linked list
        """
        if self.head is not None:
            self.head = Node(value, self.head)
            return self.head

        self.head = Node(value)
        return self.head

    def __repr__(self) -> str:
        """String representation of LinkedList. Each Node should point to the
        next with an arrow unless the list is empty or contains only one Node.
        """
        if self.head is not None:
            nodes = []
            current = self.head
            while current:
                nodes.append(str(current))
                current = current.next_
            return "-> ".join(nodes)

        return "[]"
