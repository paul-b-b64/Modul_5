class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        else:
            return False


    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        else:
            return False


    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other
        else:
            return False

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __sub__(self, value):
        self.number_of_floors -= value
        return self

    def __mul__(self, value):
        self.number_of_floors *= value
        return self

    def __floordiv__(self, value):
        self.number_of_floors //= value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


Dom1 = House('ЖК Мирный', 14)
Domik = House('IzNaKurNozh', 2)

print(Dom1)
print(Domik)

print(Domik == Dom1)
print(Domik == 2)
print(Domik == '2')

Domik = Domik + 3
print(Domik)
Domik = Domik - 2
print(Domik)
Domik = Domik * 2
print(Domik)
Domik = Domik//3
print(Domik)
Domik += 2
print(Domik)
Domik = 3 + Domik
print(Domik)

print(Domik > Dom1)
print(Domik >= Dom1)
print(Domik < Dom1)
print(Domik <= Dom1)
print(Domik != Dom1)

print(len(Dom1))
print(len(Domik))

