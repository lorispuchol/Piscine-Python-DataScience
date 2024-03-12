class calculator():

    def __init__(self, vec):
        self.vec = vec

    def __add__(self, object) -> None:
        temp = [i + object for i in self.vec]
        print(temp)
        self.vec = temp
        return temp

    def __mul__(self, object) -> None:
        temp = [i * object for i in self.vec]
        print(temp)
        self.vec = temp
        return temp

    def __sub__(self, object) -> None:
        temp = [i - object for i in self.vec]
        print(temp)
        self.vec = temp
        return temp

    def __truediv__(self, object) -> None:
        if (object == 0):
            raise BaseException
        temp = [i / object for i in self.vec]
        print(temp)
        self.vec = temp
        return temp


def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    try:
        v3 / 5
    except BaseException as e:
        print(e)


if __name__ == "__main__":
    main()
