class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("now bow")

class doberman(Dog):
    # def speak(self, sound="arf"):
    print("spund is ")
class pamerian(Dog):
    def speak(self):
        print("kow bow")
class hutch(Dog):
    def speak(self):
        print("pow bow")
class retriver(Dog):
    def speak(self, sound="awrf"):
        print("spund is ",sound )

miles = doberman("Miles", 4)
buddy = hutch("Buddy", 9)
jack = pamerian("Jack", 3)
jim = retriver("Jim", 5)
jim.speak()
print(jim.name)
print(type(miles))
print(isinstance(miles,Dog))
print(jim.species)
c=Dog("Satya",10)
print(c.speak())