import pytest

from SingleList import Node, SingleList  # Zastąp 'your_module_name' nazwą twojego modułu zawierającego klasy Node i SingleList


@pytest.fixture
def empty_list():
    return SingleList()


@pytest.fixture
def filled_list():
    s_list = SingleList()
    nodes = [Node(i) for i in range(1, 6)]  # Tworzymy węzły z danymi od 1 do 5
    for node in nodes:
        s_list.insert_tail(node)
    return s_list


def test_empty_list(empty_list):
    assert empty_list.is_empty()
    assert empty_list.count() == 0
    assert empty_list.search(5) is None
    assert empty_list.find_min() is None
    assert empty_list.find_max() is None
    with pytest.raises(ValueError):
        empty_list.remove_head()
    with pytest.raises(ValueError):
        empty_list.remove_tail()


def test_filled_list(filled_list):
    assert not filled_list.is_empty()
    assert filled_list.count() == 5
    assert filled_list.search(3).data == 3
    assert filled_list.search(10) is None
    assert filled_list.find_min().data == 1
    assert filled_list.find_max().data == 5

    removed_node = filled_list.remove_head()
    assert removed_node.data == 1
    assert filled_list.count() == 4

    filled_list.remove_tail()
    assert filled_list.count() == 3
    assert filled_list.find_max().data == 4

    filled_list.reverse()
    assert filled_list.head.data == 4
    assert filled_list.tail.data == 2

    filled_list.clear()
    assert filled_list.is_empty()
    assert filled_list.count() == 0
    assert filled_list.find_min() is None
    assert filled_list.find_max() is None
