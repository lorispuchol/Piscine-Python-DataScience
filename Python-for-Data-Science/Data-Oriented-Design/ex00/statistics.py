def mean(numbers) -> float:
    """return mean of numbers"""
    return sum(numbers) / len(numbers)


def median(numbers: tuple) -> float:
    """return median of numbers"""
    sorted_nums = sorted(numbers)
    n = len(numbers)

    if n % 2 == 1:
        # If odd, return the middle element
        return sorted_nums[n // 2]
    else:
        # If even, return the average of the two middle elements
        mid1 = n // 2
        mid2 = mid1 - 1
        return (sorted_nums[mid1] + sorted_nums[mid2]) / 2


def quartile(numbers) -> float:
    """return list with both quartile q1 and q3"""
    sorted_nums = sorted(numbers)
    n = len(numbers)

    half1 = sorted_nums[:(n//2) + (n % 2)]
    half2 = sorted_nums[(n//2):]

    q1 = median(half1)
    q3 = median(half2)

    return [q1, q3]


def std_deviation(numbers) -> float:
    """return standard deviation of numbers"""
    return pow(variance(numbers), 0.5)


def variance(numbers) -> float:
    """return variance of numbers"""
    average = mean(numbers)

    return sum([pow(abs(n - average), 2) for n in numbers]) / len(numbers)


def selection(numbers, operation) -> str:
    """select the operation to make"""
    if len(numbers) <= 0:
        return "ERROR"
    for n in numbers:
        if not isinstance(n, int | float):
            return "ERROR"
    res = 0
    if operation == "mean":
        res = mean(numbers)
    elif operation == "median":
        res = median(numbers)
    elif operation == "quartile":
        res = quartile(numbers)
    elif operation == "std":
        res = std_deviation(numbers)
    elif operation == "var":
        res = variance(numbers)
    else:
        return
    return operation + " : " + str(res)


def ft_statistics(*args, **kwargs) -> None:
    "print given statistics of list of numbers "
    operations = ("mean", "median", "quartile", "std", "var")

    for key in kwargs:
        if isinstance(kwargs[key], str) and kwargs[key] in operations:
            print(selection(args, kwargs[key]))


def main():
    "testing"
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median",
                  tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(
        5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
