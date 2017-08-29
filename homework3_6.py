class AnimalFarm:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age


class Mammals(AnimalFarm):
    def __init__(self, name, weight, age, homs):
        super().__init__(name, weight, age)
        self.homs = homs

    def homs_is(self):
        if self.homs:
            return 'рогоносец'
        else:
            return 'безрогое'


class Birds(AnimalFarm):
    def __init__(self, name, weight, age, fly, swim):
        super().__init__(name, weight, age)
        self.fly = fly
        self.swim = swim

    def fly_or_swim(self):
        if self.fly:
            return 'летающая'
        elif self.swim:
            return 'плавающая'
        else:
            return 'бегающая'


class Cow(Mammals):

    def __init__(self, name, weight, age, homs):
        super().__init__(name, weight, age, homs)

    def type_animal(self):
        return 'корова'

    def cry_animal(self):
        return 'мычит'


class Goat(Mammals):

    def __init__(self, name, weight, age, homs):
        super().__init__(name, weight, age, homs)

    def type_animal(self):
        return 'козел'

    def cry_animal(self):
        return 'блеет'


class Sheep(Mammals):

    def __init__(self, name, weight, age, homs):
        super().__init__(name, weight, age, homs)

    def type_animal(self):
        return 'баран'

    def cry_animal(self):
        return 'бекает'


class Pig(Mammals):

    def __init__(self, name, weight, age, homs):
        super().__init__(name, weight, age, homs)

    def type_animal(self):
        return 'свин'

    def cry_animal(self):
        return 'хрюкает'


class Duck(Birds):

    def __init__(self, name, weight, age, fly, swim):
        super().__init__(name, weight, age, fly, swim)

    def type_animal(self):
        return 'утка'

    def cry_animal(self):
        return 'крякает'


class Chicken(Birds):

    def __init__(self, name, weight, age, fly, swim):
        super().__init__(name, weight, age, fly, swim)

    def type_animal(self):
        return 'курица'

    def cry_animal(self):
        return 'кудахчет'


class Goose(Birds):

    def __init__(self, name, weight, age, fly, swim):
        super().__init__(name, weight, age, fly, swim)

    def type_animal(self):
        return 'гусь'

    def cry_animal(self):
        return 'гогочет'


def main():
    cow = Cow('Машка', 300, 5, True)

    goat = Goat('Сема', 20, 2, True)

    sheep = Sheep('Толик', 30, 3, True)

    pig = Pig('Борька', 50, 4, False)

    mammals = [cow, goat, sheep, pig]
    for animal in mammals:
        print('{} {} {}'.format(
            animal.type_animal(), animal.name, animal.cry_animal()))
        print('В {} живого веса на {} кг'.format(animal.name, animal.weight))
        print('Отличительный признак ', end='- ')
        print(animal.homs_is(), '\n')

    duck = Duck('Скрудж', 5, 1, True, True)

    chicken = Chicken('Ряба', 2, 1, False, False)

    goose = Goose('Степа', 10, 1, True, True)

    birds = [duck, chicken, goose]
    for bird in birds:
        print('{} {} {}'.format(
            bird.type_animal(), bird.name, bird.cry_animal()))
        print('В {} живого веса на {} кг'.format(bird.name, bird.weight))
        print('Отличительный признак ', end='- ')
        print(bird.fly_or_swim(), '\n')


main()
