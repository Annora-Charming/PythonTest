import random

class Person:
    def __init__(self):
        self.name = random.choice(names)
        self. age = random.randint(0,100)

old = []
young = []
names  = ["Biba", "Boba", "Cat", "Dog", "Boris", "Anna", "Mary"]
persons = []
for i in range(10):
    p = Person()
    persons.append(p)
for p in persons:
    if p.age >50:
        old.append(p)
    else:
        young.append(p)

print("Olds:")
for p in old:
    print (p.name, p.age)
print("Youngs:")
for p in young:
    print (p.name, p.age)




