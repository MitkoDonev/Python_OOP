class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name


class Dancer:
    def __init__(self, style):
        self.style = style


class Student(Human, Dancer):
    def __init__(self, age, name, style):
        Human.__init__(self, age, name)
        Dancer.__init__(self, style)


class Book:
    def __init__(self, price):
        self.price = price

    def __add__(self, other):
        self.price + other.price

    def __lt__(self, other):
        return self.price < other.price


john = Student(20, "John", "HipHop")
print(john.age)
print(john.name)
print(john.style)

book1 = Book(10)
book2 = Book(20)

total_price = book1 + book2
print(total_price)
compare = book1 < book2
print(compare)
