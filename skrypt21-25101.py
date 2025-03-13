class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def sound():
        print("Dźwięk zwierzęcia")

    def info(self):
        print("Informacje o zwierzęciu: \n Nazwa: ", self.name, "\n Wiek: ", self.age,"\n Płeć: ",self.sex)

class Dog(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound():
        print("Hau Hau")

    def optional_info(self):
        print("Rasa: ", self.breed)

class Cat(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound():
        print("Miau miau")

    def optional_info(self):
        print("Rasa: ", self.breed)

class Fox(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)

    def sound():
        print("Waaaaah")


if __name__ == '__main__':
    pies = Dog("Żaba", 7, "samica", "owczarek niemiecki")
    pies.info()
    pies.optional_info()
    pies.sound
    kot = Cat("Arya", 4.5, "samica", "dachowiec")
    kot.info()
    kot.optional_info()
    kot.sound
    lis = Fox("Rabuś", 4, "samiec")
    lis.info()
    lis.sound