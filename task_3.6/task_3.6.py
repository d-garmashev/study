# Необходимо реализовать классы животных на ферме:
# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси.
# Условия:
# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.


# Базовый класс должен определять общие характеристики и интерфейс.
class Animals:
    animal_name = ''
    animal_shout = '' # e.g. ga-ga for gooose
    animal_eats = ''  # e.g. grain for duck
    headcount = 0 # number of animals in farm
    legs_num = 0 # number of legs
    mass = 0 # mass of animal

    def animal_shouts(self):
        print(self.animal_shout)

    def feed_aminal(self, food_kg):
        print('Eat', food_kg, 'kg of', 'animal_eats.')

# Коровы, козы, овцы, свиньи
class AnimalsBeasts(Animals):
    needs_graze = False
    gives_meat = False
    gives_milk = False

    def take_profit(self):
        if self.gives_milk:
            print('Now you have milk.')
        elif self.gives_meat:
            print('Now you have meat.')


# Утки, куры, гуси
class AnimalsBirds(Animals):
    can_swim = False
    gives_meat = False
    gives_eggs = False

    def take_profit(self):
        if self.gives_eggs:
            print('Now you have eggs.')
        elif self.gives_meat:
            print('Now you have meat.')



# коровы
class AnimalsBeastsCow(AnimalsBeasts):
    animal_name = 'cow'
    animal_shout = 'moo'
    animal_eats = 'grain'
    legs_num = 4
    gives_milk = True


cow = AnimalsBeastsCow()
cow.headcount = 10

print(cow.animal_name, cow.__dict__)
cow.animal_shouts()
cow.take_profit()


# козы
class AnimalsBeastsGoat(AnimalsBeasts):
    animal_name = 'goat'
    animal_shout = 'mee'
    animal_eats = 'grass'
    legs_num = 4
    gives_milk = True


goat = AnimalsBeastsGoat()
goat.headcount = 3

print(goat.animal_name, goat.__dict__)
goat.animal_shouts()
goat.take_profit()


# овцы
class AnimalsBeastsSheep(AnimalsBeasts):
    animal_name = 'sheep'
    animal_shout = 'bee'
    animal_eats = 'grass'
    legs_num = 4
    gives_milk = True


sheep = AnimalsBeastsSheep()
sheep.headcount = 14

print(sheep.animal_name, sheep.__dict__)
sheep.animal_shouts()
sheep.take_profit()

# свиньи
class AnimalsBeastsPig(AnimalsBeasts):
    animal_name = 'pig'
    animal_shout = 'hru'
    animal_eats = 'grain'
    legs_num = 4
    gives_meat = True

pig = AnimalsBeastsPig()
pig.headcount = 5

print(pig.animal_name, pig.__dict__)
pig.animal_shouts()
pig.take_profit()


# утки
class AnimalsBirdsDuck(AnimalsBirds):
    animal_name = 'duck'
    animal_shout = 'krya'
    animal_eats = 'grain'
    legs_num = 2
    gives_meat = True


duck = AnimalsBirdsDuck()
duck.headcount = 7

print(duck.animal_name, duck.__dict__)
duck.animal_shouts()
duck.take_profit()


# куры
class AnimalsBirdsHen(AnimalsBirds):
    animal_name = 'hen'
    animal_shout = 'kokoko'
    animal_eats = 'grain'
    legs_num = 2
    gives_eggs = True


hen = AnimalsBirdsHen()
hen.headcount = 15

print(hen.animal_name, hen.__dict__)
hen.animal_shouts()
hen.take_profit()


# гуси
class AnimalsBirdsGoose(AnimalsBirds):
    animal_name = 'goose'
    animal_shout = 'gagaga'
    animal_eats = 'grain'
    legs_num = 2
    gives_meat = True


goose = AnimalsBirdsGoose()
goose.headcount = 9

print(goose.animal_name, goose.__dict__)
goose.animal_shouts()
goose.take_profit()