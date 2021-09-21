import pytest
from data_structures.linked_list import LinkedList

list1 = LinkedList()
list2 = LinkedList()
list3 = LinkedList()
list2.add(5)
list2.add(4)
list2.add_to_beginning(6)
list3.add("Node 1")
list3.add("Node 2")
list3.add_to_beginning("Node 0")


test_heads = [(list1.head, None), (list2.head.data, 6), (list3.head.data, "Node 0")]


@pytest.mark.parametrize("test_input, expected", test_heads)
def test_head_nodes(test_input, expected):
    assert test_input == expected


def test_add_node_empty_head():
    """When head is empty"""
    new_node = list1.add(99)

    assert new_node.data == 99
    assert list1.head.data == 99


def test_add_node_nonEmpty_head():
    """When head is non-empty"""
    list1.add(99)
    new_node = list1.add(199)

    assert new_node.data == 199
    assert list1.head.next_.next_.data == 199


def test_add_node_to_beginning_empty_head():
    list4 = LinkedList()
    list4.add_to_beginning(99)

    assert list4.head.data == 99


def test_add_node_to_beginning_nonEmpty_head():
    list1.add("three")
    list1.add_to_beginning("dew")

    assert list1.head.data == "dew"


def test_empty_list_repr(capture_stdout):
    list5 = LinkedList()
    print(list5)
    assert capture_stdout["stdout"] == "[]\n"


def test_one_node_list_repr(capture_stdout):
    list0 = LinkedList()
    list0.add(complex(0, 1))

    print(list0)
    assert capture_stdout["stdout"] == "[1j]\n"


def test_integer_list_repr(capture_stdout):
    print(list2)
    assert capture_stdout["stdout"] == "[6]-> [5]-> [4]\n"


def test_string_list_repr(capture_stdout):
    list6 = LinkedList()
    list6.add("xaxa")
    list6.add_to_beginning("axaxa")
    list6.add("xa")

    print(list6)
    assert capture_stdout["stdout"] == "[axaxa]-> [xaxa]-> [xa]\n"
