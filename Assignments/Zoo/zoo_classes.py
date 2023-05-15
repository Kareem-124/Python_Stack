class Zoo():
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals_list = []

    def display_animals_info(self):
        for i in self.animals_list:
            i.display_info()
        return self


class Animal(Zoo):
    def __init__(self, name, health, happiness,type):
        self.name = name
        self.health = health
        self.happiness = happiness
        self.type = type

    def display_info(self):
        print(f"\nAnimals Information:\
                \nType: {self.type}\
                \nName: {self.name}\
                \nHealth Level : {self.health}\
                \nHappiness Level : {self.happiness} ")
        return self

    def feed(self, health=0, happiness=0):
        self.health += (10+health)
        self.happiness += (10 + happiness)
        return self


class Lion(Animal):
    def __init__(self, name, zoo):
        super().__init__(name, 250, 50, "Lion")
        zoo.animals_list.append(self)

    def feed(self):
        super().feed(20, 10)
        print(f"\nROOOAOOR!!!! {self.happiness} / {self.health}")
        return self


class Cat(Animal):
    def __init__(self, name, zoo):
        super().__init__(name, 50, 80,"Cat")
        zoo.animals_list.append(self)

    def feed(self):
        super().feed(5, 40)
        print(f"\nMEAUOWW!!!! {self.happiness} / {self.health}")
        return self


class Bat(Animal):
    def __init__(self, name, zoo):
        super().__init__(name, 40, 50, "Bat")
        zoo.animals_list.append(self)

    def feed(self):
        super().feed(30, 10)
        print(f"\nZiiii Zii {self.happiness} / {self.health}")
        return self
