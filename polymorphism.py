class Animal:
    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Polymorphism in action
animal1 = Dog()
animal2 = Cat()
animal = Animal()
print(animal1.make_sound())
print(animal2.make_sound())
print(animal.make_sound())

