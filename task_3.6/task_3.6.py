# Необходимо реализовать классы животных на ферме:
#
# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси.
# Условия:
#
# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.


# Базовый класс должен определять общие характеристики и интерфейс.
class FarmAnimals:
    animal_shout = '' # e.g. ga-ga for gooose
    animal_eats = ''  # e.g. grain for duck
    headcount = 0 # number of animals in farm
    legs_num = 0 # number of legs
    mass = 0 # mass of animal
    gives_milk = False
    gives_meat = False
    gives_eggs = False

    def animal_shouts(self):
        print(self.animal_shout)

    def feed_aminal(self, food_kg):
        print('Eat',food_kg,'kg of','animal_eats.')

    def take_profit(self):
        if self.gives_milk:
            print('Now you have milk.')
        elif self.gives_eggs:
            print('Now you have eggs.')
        elif self.gives_meat:
            print('Now you have meat.')
        else:
            print('The animal is not for milk or meat.')


# Коровы, козы, овцы, свиньи
class FarmAnimalsBeasts(FarmAnimals):
    needs_graze = False


# Утки, куры, гуси
class FarmAnimalsBirds(FarmAnimals):
    can_swim = False

# коровы

cow = FarmAnimalsBeasts()
cow.animal_shout = 'moo'
cow.animal_eats = 'grain'
cow.headcount = 10
cow.legs_num = 4
cow.gives_milk = True

print(cow.__dict__)
cow.animal_shouts()
cow.take_profit()

# козы

goat = FarmAnimalsBeasts()
goat.animal_shout = 'mee'
goat.animal_eats = 'grass'
goat.headcount = 3
goat.legs_num = 4
goat.gives_milk = True

print(goat.__dict__)
goat.animal_shouts()
goat.take_profit()


# овцы

sheep = FarmAnimalsBeasts()
sheep.animal_shout = 'bee'
sheep.animal_eats = 'grass'
sheep.headcount = 14
sheep.legs_num = 4
sheep.gives_meat = True

print(sheep.__dict__)
sheep.animal_shouts()
sheep.take_profit()


# свиньи

pig = FarmAnimalsBeasts()
pig.animal_shout = 'hru'
pig.animal_eats = 'grain'
pig.headcount = 5
pig.legs_num = 4
pig.gives_meat = True

print(pig.__dict__)
pig.animal_shouts()
pig.take_profit()


# утки

duck = FarmAnimalsBirds()
duck.animal_shout = 'crya'
duck.animal_eats = 'grain'
duck.headcount = 7
duck.legs_num = 2
duck.gives_meat = True

print(duck.__dict__)
duck.animal_shouts()
duck.take_profit()

# куры

hen = FarmAnimalsBirds()
hen.animal_shout = 'kokoko'
hen.animal_eats = 'grain'
hen.headcount = 15
hen.legs_num = 2
hen.gives_eggs = True

print(hen.__dict__)
hen.animal_shouts()
hen.take_profit()

# гуси

goose = FarmAnimalsBirds()
goose.animal_shout = 'gaga'
goose.animal_eats = 'grain'
goose.headcount = 9
goose.legs_num = 2
goose.gives_meat = True

print(goose.__dict__)
goose.animal_shouts()
goose.take_profit()