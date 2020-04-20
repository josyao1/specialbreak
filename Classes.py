
class Animal:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = int(age)

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAge(self):
        return self.age

    def toString(self):
        return self.name + " is a " + self.type + " that is " + str(self.age) + " years old"

    def growOlder(self):
        self.age += 1
        return self.name + " is now " + str(self.age) + " years old"


class Dog(Animal):

    def __init__(self, name, type, age):
        super().__init__(name, type, age)
        self.tricks = []

    def learnTrick(self, trick):
        self.tricks.append(trick)

    def do(self, trick):
        if trick in self.tricks:
            return self.name + " did " + trick
        else:
            return self.name + " doesn't know how to " + trick


kek = Dog("KeKe", "Pomeranian", "6")
kek.learnTrick("eat")
print(kek.toString())
print(kek.do("exercise"))

