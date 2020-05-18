from pkg.search import binary_search


def test_binary_search():
    order_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert binary_search(order_list, 1) == True
    assert binary_search(order_list, 2) == True

    assert binary_search(order_list, 8) == True
    assert binary_search(order_list, 9) == True

    assert binary_search(order_list, 10) == False


def test_binary_with_large_list():
    order_list = list(range(1, 10000))
    assert binary_search(order_list, 1) == True
    assert binary_search(order_list, 100) == True
    assert binary_search(order_list, 1000) == True

    assert binary_search(order_list, 10001) == False
    assert binary_search(order_list, 20000) == False
