def binary_search(list_, value):
    """This function performs a binary search.
    """
    first = 0
    last = len(list_) - 1

    while first <= last:
        middle = first + (last - first) // 2
        if value == list_[middle]:
            return middle
        elif value < list_[middle]:
            last = middle - 1
        else:
            first = middle + 1
    return None


def linear_search(list_, value):
    for i, item in enumerate(list_):
        if item == value:
            return i
    return None


if __name__ == "__main__":
    assert binary_search(range(10), 5) == 5
    assert binary_search(range(3), 1) == 1
    assert binary_search(range(10), 10) == None
    assert binary_search([], 1) == None
    assert binary_search(range(3), 2) == 2

    assert linear_search(range(10), 5) == 5
    assert linear_search(range(3), 1) == 1
    assert linear_search(range(10), 10) == None
    assert linear_search([], 1) == None
