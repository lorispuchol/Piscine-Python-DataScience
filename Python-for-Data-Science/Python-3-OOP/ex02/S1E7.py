from S1E9 import Character


class Baratheon(Character):
    """docstring for Baratheon Class"""

    def __init__(self, first_name, is_alive=True):
        """docstring for Baratheon Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """docstring for Baratheon die method"""
        self.is_alive = False

    def __str__(self) -> str:
        """Return class informations"""
        return Character.__str__(self)

    def __repr__(self) -> str:
        """Return class informations"""
        return Character.__repr__(self)


class Lannister(Character):
    """docstring for Lannister Class"""

    def __init__(self, first_name, is_alive=True):
        """docstring for Lanister Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """Return class informations"""
        return Character.__str__(self)

    def __repr__(self) -> str:
        """Return class informations"""
        return Character.__repr__(self)

    def die(self):
        """docstring for Lanister die method"""
        self.is_alive = False

    @staticmethod
    def create_lannister(name, isAlive):
        """create Lannister from Laniister Class outside an instance"""
        return Lannister(name, isAlive)


def main():
    """testing"""
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(
        f"Name : {Jaine.first_name, type(Jaine).__name__},\
 Alive : {Jaine.is_alive}"
    )


if __name__ == "__main__":
    main()
