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

    def __mul__(self, object) -> None:
        """overload multiplication"""
        temp = [i * object for i in self.vec]
        print(temp)
        self.vec = temp

    def __sub__(self, object) -> None:
        """overload substraction"""
        temp = [i - object for i in self.vec]
        print(temp)
        self.vec = temp

    def __truediv__(self, object) -> None:
        """overload division"""
        if (object == 0):
            return
        temp = [i / object for i in self.vec]
        print(temp)
        self.vec = temp


def main():
    "testing"
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5


if __name__ == "__main__":
    main()
