def square(x: int | float) -> int | float:
    """returns the value of x squared"""
    return x**2


def pow(x: int | float) -> int | float:
    """returns the value of x exponent x"""
    return x**x


def outer(x: int | float, function) -> object:
    """outter"""
    count = 0
    count += 1

    def inner() -> float:
        """inner"""
        nonlocal x
        x = function(x)
        return x

    return inner


def main():
    """testing"""
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
