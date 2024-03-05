def contain_a(item):
    '''
    Return true if "a" is in the item
    '''
    if 'a' in item:
        return True
    return False


def contain_b(item):
    '''
    Return true if "b" is in the item
    '''
    if 'b' in item:
        return True
    return False


def ft_filter(ft_function, ft_it):
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    newList = (x for x in ft_it if ft_function(x))
    return newList


def main():
    '''Main de test'''

    ft_list = ["apple", "banana", "cherry", "apple", "cherry"]
    ft_list2 = ["apple", "banana", "cherry", "apple", "cherry"]
    print(list(filter(contain_b, ft_list)))
    print(list(filter(contain_a, ft_list)))
    print(list(ft_filter(contain_b, ft_list2)))
    print(list(ft_filter(contain_a, ft_list2)))


if __name__ == "__main__":
    main()
