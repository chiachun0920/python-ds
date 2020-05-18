def binary_search(order_list, value):
    if len(order_list) == 1:
        return order_list[0] == value
    mid = (len(order_list)) // 2
    if order_list[mid] > value:
        return binary_search(order_list[:mid], value)
    elif order_list[mid] < value:
        return binary_search(order_list[mid + 1:], value)
    else:
        return True
