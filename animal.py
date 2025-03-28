# Animal Sounds Parent class: Animal with method make_sound(), Child classes: Dog, Cat, Cow override the sound

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Cow(Animal):
    def make_sound(self):
        return "Moo"

dog = Dog()
cat = Cat()
cow = Cow()

print("Dog Sound:", dog.make_sound())
print("Cat Sound:", cat.make_sound())
print("Cow Sound:", cow.make_sound())
