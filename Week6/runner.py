from animalclass import Animal, Dog

animal_one = Animal("Kali","F", 65, 4)
animal_two = Animal("Tammy","F", 7, 7)

print("Animal GetName result is: ", Animal.getName(animal_one), "\n")
print("Animal IsFemale result is: ", Animal.isFemale(animal_one), "\n")
print("Animal GetName result is: ", Animal.getName(animal_two), "\n")
print("Animal IsFemale result is: ", Animal.isFemale(animal_two), "\n")

dog_one = Dog("Max", "M", 45, 15, 5)
dog_two = Dog("Gina", "F", 20, 10, 24)
print("Animal GetName result is: ", Dog.getName(dog_one), "\n")
print("Animal IsFemale result is: ", Dog.isFemale(dog_one), "\n")
print("Animal GetName result is: ", Dog.getName(dog_two), "\n")
print("Animal IsFemale result is: ", Dog.isFemale(dog_two), "\n")