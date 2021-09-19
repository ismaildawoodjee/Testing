class Node:
    def __init__(self, data=None, next_=None):
        """Node object to hold data.

        Args:
            data (any, optional): data in the node. Defaults to None.
            next_ (Node, optional): pointer to next node. Defaults to None.
        """
        self.data = data
        self.next_ = next_

    def __repr__(self) -> str:
        if self.data is None:
            return "[]"
        return f"[{self.data}]"
