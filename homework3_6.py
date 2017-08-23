class AnimalFarm:
    def __init__(self, name, weight, age, type_animal, cry):
        self.name = name
        self.weight = weight
        self.age = age
        self.type_animal = type_animal
        self.cry = cry

    def how_cry(self):
        print('{}'.format(self.cry))


class Mammals(AnimalFarm):
    def __init__(self, name, weight, age, type_animal, cry, homs):
        super().__init__(name, weight, age, type_animal, cry)
        self.homs = homs

    def homs_is(self):
        if self.homs:
            print('рогоносец')
        elif self.age >= 3:
            print('бекон')
        else:
            print('поросенок')


class Birds(AnimalFarm):
    def __init__(self, name, weight, age, type_animal,cry, fly, swim):
        super().__init__(name, weight, age, type_animal, cry)
        self.fly = fly
        self.swim = swim

    def fly_or_swim(self):
        if self.fly:
            print('летающая')
        elif self.swim:
            print('плавающая')
        else:
            print('бегающая')


cow = Mammals('Машка', 300, 5, 'корова', 'мычит', True)

goat = Mammals('Сема', 20, 2, 'козел', 'блеет', True)

sheep = Mammals('Толик', 30, 3, 'баран', 'бекает', True)

pig = Mammals('Борька', 50, 4, 'свин', 'хрюкает', False)

mammals = [cow, goat, sheep, pig]
for animal in mammals:
    print('{} {} {}'.format(animal.type_animal, animal.name, animal.cry))
    print('В {} живого веса на {} кг'.format(animal.name, animal.weight))
    print('Отличительный признак ', end='- ')
    print(animal.homs_is(), '\n')


duck = Birds('Скрудж', 5, 1, 'утка', 'крякает', True, True)

chicken = Birds('Ряба', 2, 1, 'курица', 'кудахчет', False, False)

goose = Birds('Степа', 10, 1, 'гусь', 'гогочет', True, True)

birds = [duck, chicken, goose]
for bird in birds:
    print('{} {} {}'.format(bird.type_animal, bird.name, bird.cry))
    print('В {} живого веса на {} кг'.format(bird.name, bird.weight))
    print('Отличительный признак ', end='- ')
    print(bird.fly_or_swim(), '\n')
