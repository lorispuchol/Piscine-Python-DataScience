from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """docstring for King Class"""

    def set_eyes(self, eyes_color):
        '''change eye color'''
        self.eyes = eyes_color

    def set_hairs(self, hairs_color):
        '''change hair color'''
        self.hairs = hairs_color

    def get_eyes(self):
        '''return eye color'''
        return self.eyes

    def get_hairs(self):
        '''return hair color'''
        return self.hairs


def main():
    """testing"""
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
