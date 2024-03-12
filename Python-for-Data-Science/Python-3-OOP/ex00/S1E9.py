from abc import ABC, abstractmethod


class Character(ABC):

    '''docstring for Character abstract Class'''
    @abstractmethod
    def abstarctor():
        '''to make the class abstract'''
        pass

    # @abstractmethod
    def __init__(self, first_name, is_alive=True):
        '''Your docstring for Character abstract Constructor'''
        self.first_name = first_name
        self.is_alive = is_alive
        # pass

    # @abstractmethod
    def die(self):
        '''Your docstring for Character abstract Method'''
        self.is_alive = False
        # pass


class Stark(Character):

    '''docstring Stark for Class'''
    def abstarctor():
        '''to make the class abstract'''
        pass

# class Character(ABC):

#     '''Your docstring for abstract Class'''

#     @abstractmethod
#     def __init__(self, first_name, is_alive=True):
#         '''Your docstring for abstract Constructor'''
#         pass

#     @abstractmethod
#     def die(self):
#         '''Your docstring for abstract Method'''
#         pass


# class Stark(Character):

#     '''Your docstring for Class'''

#     def __init__(self, first_name, is_alive=True):
#         '''Your docstring for Constructor'''
#         self.first_name = first_name
#         self.is_alive = is_alive

#     def die(self):
#         '''Your docstring for Method'''
#         self.is_alive = False


def main():
    """testing"""
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
    # hodor = Character("hodor")


if __name__ == "__main__":
    main()
