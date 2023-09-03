class Daon:
    def __init__(self, width = 0.0, length = 0.0, species = "", addition = None):
        self.width = width
        self.length = length
        self.species = species
        self.addition = None

    def define_species(self):
        try:
            if self.width < 2.9 or self.length < 5.1:
                self.species = "small-leaf"
            elif self.width >= 2.9 and self.length >= 5.1:
                self.species = "big-leaf"
        except ValueError:
            if ValueError == self.width and self.length < 5.1:
                self.species = "small-leaf"
            elif ValueError == self.width and self.length >= 5.1:
                self.species = "big-leaf"
            elif ValueError == self.length and self.width < 2.9:
                self.species = "small-leaf"
            elif ValueError == self.length and self.width >= 2.9:
                self.species = "big-leaf"


