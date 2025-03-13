class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def sound(self):
        print(self.name, " is barking!")

if __name__ == '__main__':
    reksio = Dog("Reksio", 3, "brązowy")
    tofik = Dog("Tofik", 6, "czarny")
    fafik = Dog("Fafik", 1, "biały")

    reksio.sound()
    tofik.sound()
    fafik.sound()
