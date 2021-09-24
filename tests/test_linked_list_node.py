import pytest
from data_structures.linked_list import Node

a1 = Node()
b1 = Node(5)
c2 = Node("aaaa")
c1 = Node(False, c2)

test_cases = [
    (a1.data, None),
    (b1.data, 5),
    (b1.next_, None),
    (c1.data, False),
    (c1.next_, c2),
    (c1.next_.data, c2.data),
    (c1.next_.data, "aaaa"),
]


@pytest.mark.parametrize("test_input, expected", test_cases)
def test_multiple_cases(test_input, expected):
    assert test_input == expected


def test_empty_node():
    assert a1.data is None


def test_data_node():
    assert b1.data == 5


def test_next_node():
    assert b1.next_ is None
    assert c1.next_ == c2


def test_next_node_data():
    assert c1.next_.data == c2.data
    assert c1.next_.data == "aaaa"


def test_empty_node_repr(capture_stdout):
    print(a1)
    assert capture_stdout["stdout"] == "[]\n"


def test_data_node_repr(capture_stdout):
    print(b1)
    assert capture_stdout["stdout"] == "[5]\n"


def test_next_node_repr(capture_stdout):
    print(c1.next_)
    assert capture_stdout["stdout"] == "[aaaa]\n"
