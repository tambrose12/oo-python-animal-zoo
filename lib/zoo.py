from lib.animal import Animal


class Zoo:
    all = []

    def __init__(self, name, location):
        self.name = name
        self.location = location
        Zoo.all.append(self)

    @property
    def animals(self):
        # new_list_of_animals_in_our_zoo = []
        # for animal in Animal.all:
        #     if animal.zoo == self:
        #         new_list_of_animals_in_our_zoo.append(animal)
        # return new_list_of_animals_in_our_zoo
        return [a for a in Animal.all if a.zoo == self]

    @property
    def animal_species(self):
        return list({a.species for a in self.animals})

    def find_by_species(self, species):
        return [a for a in self.animals if a.species == species]

    @property
    def animal_nicknames(self):
        return [a.nickname for a in self.animals]

    @classmethod
    def find_by_location(cls, location):
        return [z.name for z in cls.all if z.location == location]
