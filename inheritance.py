class Employee:
    raise_percentage = 1.04

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name.upper()}.{last_name.upper()}@email.net"
        self.salary = salary

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.salary = int(self.salart * self.raise_percentage)


class Developer(Employee):
    raise_percentage = 1.15

    def __init__(self, first_name, last_name, salary, programming_language):
        super().__init__(first_name, last_name, salary)
        self.programming_language = programming_language


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name, salary)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print(f"--> {employee.full_name()}")


dev1 = Developer("Arnold", "Askarpovich", 45000, "C++")
dev2 = Developer("Corey", "Schaefer", 37000, "Kotlin")
# print(help(dev1))
# print(dev1.email)
# print(dev1.programming_language)
manager1 = Manager("Silvia", "Smith", 90000, [dev1])
# print(manager1.email)
# manager1.print_employees()
manager1.add_employee(dev2)
manager1.print_employees()

print(isinstance(manager1, Manager))
print(issubclass(Developer, Employee))
