import pytest


@pytest.fixture
def unordered_list():
    from pkg.basic import UnorderedList
    return UnorderedList()


def test_unordered_list_adding_item(unordered_list):
    assert unordered_list.head is None
    assert unordered_list.is_empty() is True
    assert unordered_list.size() is 0

    unordered_list.add(7)

    assert unordered_list.head is not None
    assert unordered_list.head.data is 7
    assert unordered_list.head.next is None
    assert unordered_list.size() is 1
    assert unordered_list.search(7) is True
    assert unordered_list.search(8) is False

    unordered_list.add('A')

    assert unordered_list.head.data is 'A'
    assert unordered_list.head.next.data is 7
    assert unordered_list.head.next.next is None
    assert unordered_list.size() is 2
    assert unordered_list.search('A') is True
    assert unordered_list.search('B') is False


def test_unordered_list_removing_item(unordered_list):
    unordered_list.add('foo')
    unordered_list.add('bar')
    unordered_list.add('goo')
    unordered_list.add('gle')

    assert unordered_list.size() == 4

    unordered_list.remove('gle')

    assert unordered_list.size() == 3
    assert unordered_list.search('gle') == False

    unordered_list.remove('foo')
    assert unordered_list.size() == 2
    assert unordered_list.search('foo') == False
