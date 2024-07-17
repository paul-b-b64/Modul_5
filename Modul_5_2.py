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
        a = f'Название:', {self.name},'количество этажей:', {self.number_of_floors}
        return a



Dom1 = House('ЖК Мирный', 14)
Dom2 = House('Платан-Строй', 24)

print(Dom1)

print(len(Dom1))
print(len(Dom2))
# Dom1.go_to(7)