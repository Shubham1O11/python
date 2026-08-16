class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    pass

    @staticmethod
    def bark():
        print("Bow Bow")

d=Dog()
d.bark()
