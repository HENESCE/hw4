class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        name = args[0]
        cls.houses_history.append(name)
        return object.__new__(cls)

    def __init__(self, name, number_of_floors,):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он станется в истории ")

    def go_to(self, new_floor):
            if 0 < new_floor <= self.number_of_floors:
                for floor in range(1, new_floor + 1):
                    print(floor)
            else:
                print("Такого этажа не существует")
    def __len__(self,):
        return self.number_of_floors

    def __str__(self):
        return f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}.'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, other):
        return self + other

    def __radd__(self, other):
        return self + other



h1 = House("ЖК Фили", 18)
print(House.houses_history)
h2 = House("Домик в деревне", 1)
print(House.houses_history)
h3 = House("ЖК Азбука", 24)
print(House.houses_history)

del h2
del h3

print(House.houses_history)




