from zoo_classes import *
lion = []
cat = []
bat = []
zoo = Zoo("Nablus")

lion.append(Lion("Simpa",zoo))
lion[0].feed()

cat.append(Cat("Lelo", zoo))
cat[0].feed()

bat.append(Bat("Flyer", zoo))
lion.append(Lion("Mora", zoo))
lion.append(Lion("Zack", zoo))
zoo.display_animals_info()

