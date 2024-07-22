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


Dom1 = House('ЖК Мирный', 14)
Domik = House('IzNaKurNozh', 2)

# Dom1.go_to(7)
# Domik.go_to(3)

print(Dom1)
print(Domik)

print(len(Dom1))
print(len(Domik))
