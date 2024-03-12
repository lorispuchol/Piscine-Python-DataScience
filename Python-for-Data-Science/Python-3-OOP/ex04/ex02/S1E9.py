from abc import ABC, abstractmethod


class Character(ABC):

    '''Your docstring for abstract Class'''

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        '''Your docstring for abstract Constructor'''
        self.first_name = first_name
        self.is_alive = is_alive
        pass

    @abstractmethod
    def die(self):
        '''Your docstring for abstract Method'''
        self.is_alive = False

    def __str__(self):
        '''Your docstring for abstract Method'''
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Your docstring for Method"""
        return self.__str__()


class Stark(Character):
    '''Your docstring for Stark Class'''

    def __init__(self, first_name, is_alive=True):
        '''Your docstring for Stark Constructor'''
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        '''Your docstring for Stark Method'''
        self.is_alive = False
