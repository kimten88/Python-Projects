#Creating the parent class
class Animal:
    #to know the name of the animal
    species = "Species Name"
    #understand dietary needs/subclassification
    diet = "Herbivore/Omnivore/Carnivore"
    #subclassification if the animal is endangered or not
    endangered = "Yes/No"
    #subclassification if the animal is a vertibrate or an invertibrate
    spine = "Vertibrate/Invertibrate"

#aimmals in marine life have unique characteristics
class Marine(Animal):
    #to identify the unique environment of the animal's habitation
    ocean_zone = "Sunlight/Twilight/Midnight/Abyss and Trenches"
    #coral reefs are unique environments which require different consideration
    reef_resident = "Yes/No"


class Mammal(Animal):
    #time period from conception to birth
    gestation_period = "123days"
    #mammals live in all different environments
    terrain = "Land/Air/Water"
    
