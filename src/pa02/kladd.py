""""
class Person:
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname

class Member(Person):
    def __init__(self, firstname, surname):
        super().__init__()

p = Person('Clark', 'Anderson')
m = Member(p)
print(m.firstname)
"""


class Board:
    def __init__(self, chutes, ladders):
        self.chutes = chutes
        self.ladders = ladders


class Player(Board):
    def __init__(self, chutes, ladders):
        super().__init__(chutes, ladders)


p = Player([(3, 2), (5, 1)], [(2, 4), (3, 5)])

print(p.chutes)