import random


class Person:
    def __init__(self):
        self.name = random.choice(names)
        self.age = random.randint(0, 101)


old = []
young = []
names = ["Biba", "Boba", "Cat", "Dog", "Boris", "Anna", "Mary"]
persons = []
for i in range(10):
    p = Person()
    persons.append(p)
for p in persons:
    if p.age > 50:
        old.append(p)
    else:
        young.append(p)

print("Olds:")
for p in old:
    print(p.name, p.age)
print("Youngs:")
for p in young:
    print(p.name, p.age)

print("Dogs")
# Parent class
class Dog:
    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class (inherits from Dog class)
class Puddle(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog class)
class YorkshireTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


Dog1 = Puddle("Boba", 8)
Dog2 = YorkshireTerrier("Kitty", 5)
Dogs_list = [Dog1, Dog2]


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def max(*args):
        w_max = 0
        for arg.weight in args():
            if (arg.weight > w_max):
                w_max = arg.weight
        return arg.name, arg.weight


dog1 = Dog("Cat", 8, 10)
dog2 = Dog("Skunk", 3, 12)
dog3 = Dog("Shark", 5, 20)
print("The heaviest one:", max(dog1.weight, dog2.weight, dog3.weight))
