import pytest


@pytest.fixture
def unordered_list():
    from pkg.basic import UnorderedList
    return UnorderedList()


def test_unordered_list(unordered_list):
    assert unordered_list.head is None
    assert unordered_list.is_empty() is True

    unordered_list.add(7)

    assert unordered_list.head is not None
