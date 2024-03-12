from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def set_eyes(self, eyes_color):
        self.eyes = eyes_color

    def set_hairs(self, hairs_color):
        self.hairs = hairs_color

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs


def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
