from enum import Enum
class species(Enum):
    small_leaf = 1
    big_leaf = 2

# list spesies = [species(small), mid, big]

# small : 
#     nama : 'small-leaf',
#     ba_p : ...
#     ba_l : ...
#     bb_p : ...
#     bb_l : ...

# dict_priority {

# }

# species = {
#     "small-leaf": 1,
#     "big-leaf": 2
# }
class Daon:
    def __init__(self, width = "-", length = "-", species = "???", addition = None):
        self.width = width
        self.length = length
        self.species = species
        self.addition = addition

    def define_species(self):
        try:
            if self.width < 2.9 or self.length < 5.1:
                self.species = species.small_leaf.name.replace("_", "-")
            elif self.width >= 2.9 and self.length >= 5.1:
                self.species = species.big_leaf.name.replace("_", "-")
        except:
            if "-" == self.width and self.length < 5.1:
                self.species = species.small_leaf.name.replace("_", "-")
            if "-" == self.width and self.length > 5.1:
                self.species = species.big_leaf.name.replace("_", "-")
            if "-" == self.length and self.width < 2.9:
                self.species = species.small_leaf.name.replace("_", "-")
            if "-" == self.length and self.width >= 2.9:
                self.species = species.big_leaf.name.replace("_", "-")

    def tolist(self):
        if self.addition != None:
            return [self.width, self.length, self.species, self.addition]
        return [self.width, self.length, self.species]
