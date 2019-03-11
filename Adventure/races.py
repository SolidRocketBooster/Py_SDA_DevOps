'''

'''

class Creature():
    def __init__(self, hp=1, *args, **kwargs):
        self.hp = hp


class Humanoid(Creature):
    def __init__(self, name='', hp=10):
        super(Humanoid, self).__init__(hp=hp)
        self.name = name

    def __str__(self):
        return f"{type(self).__name__}: {self.name}"


class Elf(Humanoid):
    pass


class Human(Humanoid):
    pass


class Dwarf(Humanoid):
    pass


class Halfling(Humanoid):
    pass


class Orc(Humanoid):
    pass

