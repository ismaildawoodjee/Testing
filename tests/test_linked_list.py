import pytest
from data_structures.linked_list import Node

a1 = Node()
b1 = Node(5)
c2 = Node(4)
c1 = Node(3, c2)

def test_linked_list_node():
    assert a1.data == None
