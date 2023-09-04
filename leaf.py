from enum import Enum


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
    def __init__(self, width = 0.0, length = 0.0, species = "undefined-species", addition = None):
        self.width = width
        self.length = length
        self.species = species
        self.addition = addition

    def define_species(self, species ):
        # try:
        if self.width != 0.0 and self.length != 0.0:
            for i in range(len(species)):
                if self.width >= species[i].min_width and self.width <= species[i].max_width:
                    if self.length >= species[i].min_length and self.length <= species[i].max_length:
                        self.species = species[i].name
                        if self.addition != None:
                            self.define_addition(species)
                        break
                    else:
                        if self.width *  self.length >= species[i].min_area and self.width * self.length <= species[i].max_area:
                            self.species = species[i].name
                            if self.addition != None:
                                self.define_addition(species)
                            break
                elif self.length >= species[i].min_length and self.length <= species[i].max_length:
                    if self.width * self.length >= species[i].min_area and self.width * self.length <= species[i].max_area:
                        self.species = species[i].name
                        break

        elif self.width == 0.0 or self.length == 0.0:
            for i in range(len(species)):
                if self.width == 0.0:
                    if self.length >=  species[i].min_length and self.length <= species[i].max_length:
                        self.species = species[i].name
                        if self.addition != None:
                            self.define_addition(species)
                        break
                if self.length == 0.0:
                    if self.width >= species[i].min_width and self.width <=species[i].max_width:
                        self.species = species[i].name
                        if self.addition != None:
                            self.define_addition(species)
                        break
        # try:
        #     if self.width < 2.9 or self.length < 5.1:
        #         self.species = species.small_leaf.name.replace("_", "-")
        #     elif self.width >= 2.9 and self.length >= 5.1:
        #         self.species = species.big_leaf.name.replace("_", "-")
        # except:
        #     if "-" == self.width and self.length < 5.1:
        #         self.species = species.small_leaf.name.replace("_", "-")
        #     if "-" == self.width and self.length > 5.1:
        #         self.species = species.big_leaf.name.replace("_", "-")
        #     if "-" == self.length and self.width < 2.9:
        #         self.species = species.small_leaf.name.replace("_", "-")
        #     if "-" == self.length and self.width >= 2.9:
        #         self.species = species.big_leaf.name.replace("_", "-")

    def tolist(self):
        if self.addition != None:
            return [self.width, self.length, self.species, self.addition]
        return [self.width, self.length, self.species]

    def define_addition(self, species):
        for i in range(len(species)):
            if self.species == 'small-leaf' :
                self.addition = 'round'
                break
            elif self.species == 'big-leaf':
                self.addition = 'square'
                break
