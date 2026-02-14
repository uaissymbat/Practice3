class Flyer:
    def fly(self):
        return "Flying high!"

class Swimmer:
    def swim(self):
        return "Swimming deep!"

class Duck(Flyer, Swimmer):
    pass

# Or a more complex example with overlapping methods
class A:
    def process(self):
        return "A"

class B(A):
    def process(self):
        return "B"

class C(A):
    def process(self):
        return "C"

class D(B, C):
    pass

# Usage
duck = Duck()
print(duck.fly())   # Flying high!
print(duck.swim())  # Swimming deep!

# MRO demonstration
obj = D()
print(obj.process())      # "B" (due to MRO: D -> B -> C -> A)
print(D.__mro__)          # Shows the method resolution order