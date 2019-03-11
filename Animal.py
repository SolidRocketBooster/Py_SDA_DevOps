class Animal(object):
    count = 0
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age


    def who_am_i(self):
        print(f'My name is {self.name}. I have {self.age} years.')


class Cat(Animal):
    def meow(self):
        print()


class Dog(Animal):
    def bark(self):
        print('Bark!')


    def who_am_i(self):
        print('I\'m doge!')


class Chimera(Cat, Dog):
    def who_am_i(self):
        super(Cat, self).who_am_i()

    def __str__(self):
        print('Chimera')

