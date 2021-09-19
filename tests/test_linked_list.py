import pytest
from data_structures.linked_list import Node

a1 = Node()
b1 = Node(5)
c2 = Node(4)
c1 = Node(3, c2)

test_cases = [
    (a1.data, None),
    (b1.data, 5),
    (b1.next_, None),
    (c1.next_, c2),
    (c1.next_.data, c2.data),
    (c1.next_.data, 4),
]


def test_empty_node():
    assert a1.data == None


def test_data_node():
    assert b1.data == 5


# TODO: use parametrize decorator
# def test_data_node(test_case, expected):
#     assert Node(test_case).data == expected


def test_next_node():
    assert b1.next_ == None
    assert c1.next_ == c2


def test_next_node_data():
    assert c1.next_.data == c2.data
    assert c1.next_.data == 4


# TODO: parametrize decorator with many test cases
def test_multiple_nodes():
    assert b1.data == 5


# TODO: test for stdout when printing string repr of Node
def test_empty_node_repr(capture_stdout):
    print(a1)
    assert capture_stdout["stdout"] == "[]\n"


def test_data_node_repr(capture_stdout):
    print(b1)
    assert capture_stdout["stdout"] == "[5]\n"


def test_next_node_repr(capture_stdout):
    print(c1.next_)
    assert capture_stdout["stdout"] == "[4]\n"
