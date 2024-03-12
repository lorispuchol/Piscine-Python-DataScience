class calculator():
    """Calculator class"""

    def __init__(self, vec):
        """Calculator Constructor Class"""
        self.vec = vec

    def __add__(self, object) -> None:
        """overload addition"""
        temp = [i + object for i in self.vec]
        print(temp)
        self.vec = temp
        return temp

    # decorator
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """dot product"""
        print("Dot product is:", sum(i[0] * i[1] for i in zip(V1, V2)))

    # decorator
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """add"""
        print("Add Vector is :", [i[0] + i[1] for i in zip(V1, V2)])

    # decorator
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """sous"""
        print("Sous Vector is :", [i[0] - i[1] for i in zip(V1, V2)])


def main():
    """testing"""
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
