def calculate() -> float:
    pass


def selection(*numbers, operation) -> str:
    if len(numbers <= 0):
        return "ERROR"
    for n in numbers:
        if not isinstance(n, int | float):
            return "ERROR"


def ft_statistics(*args, **kwargs) -> None:

    operations = ("mean", "median", "quartile", "std", "var")

    for key in kwargs:
        if isinstance(kwargs[key], str) and kwargs[key] in operations:
            print(selection(args, kwargs[key]))


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
