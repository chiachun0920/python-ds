from pkg.basic import Node


def test_node_construct():
    node = Node(9)
    assert node is not None
    assert node.data is 9
    assert node.next is None
