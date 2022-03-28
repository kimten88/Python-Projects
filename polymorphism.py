#Creating the parent class
class Animal:
    #to know the name of the animal
    entry_species = "Species Name"
    #understand dietary needs/subclassification
    entry_diet = "Herbivore/Omnivore/Carnivore"
    #where the animal resides
    entry_ecosystem = "Unknown"
    
    def information(self):
        entry_species = input("Enter the animal's species type: ")
        entry_diet = input("Is this animal a Herbivore, Omnivore, or Carnivore? ")
        entry_ecosystem = input("Enter the type of ecosystem this animal resides in: ")
        msg = "\nSpecies {}\nDiet {} \nEcosystem {}".format(self.entry_species, self.entry_diet, self.entry_ecosystem)
        return msg

#aimmals in marine life have unique characteristics
class Marine(Animal):
    #to identify the unique environment of the animal's habitation
    entry_ocean_zone = "Sunlight/Twilight/Midnight/Abyss and Trenches"
    #coral reefs are unique environments which require different consideration
    entry_reef_resident = "Yes/No"

    #Same method as the parent class "Animal" but ecosystem is now ocean_zone
    def information(self):
        entry_species = input("Enter the animal's species type: ")
        entry_diet = input("Is this animal a Herbivore, Omnivore, or Carnivore? ")
        entry_ocean_zone = input("Enter the ocean zone this animal resides in: ")
        msg = "\nSpecies {}\nDiet {} \nOcean Zone {}".format(self.entry_species, self.entry_diet, self.entry_entry_ocean_zone)
        return msg


class Mammal(Animal):
    #time period from conception to birth
    entry_gestation_period = "123days"
    #mammals live in all different environments
    entry_terrain = "Land/Air/Water"

    #Same method as the parent class "Animal" but ecosystem is now terrain
    def information(self):
        entry_species = input("Enter the animal's species type: ")
        entry_diet = input("Is this animal a Herbivore, Omnivore, or Carnivore? ")
        entry_terrain = input("Enter which terrain/terriains can this mammal survive in : ")
        msg = "\nSpecies {}\nDiet {} \nTerrain {}".format(self.entry_species, self.entry_diet, self.entry_terrain)
        return msg

if __name__ =='__main__':
    animal = Animal()
    animal.information()

    marine = Marine()
    marine.information()

    mammal = Mammal()
    mammal.information()

