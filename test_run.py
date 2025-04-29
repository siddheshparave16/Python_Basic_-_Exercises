
class Employee:
    def set_data(self, n: str, a: int, s: float):
        self.name = n
        self.age = a
        self.salary = s

    def display(self):
        print(f"Employee name: {self.name}, Employee Age: {self.age}, Employee salary: {self.salary}")


emp1 = Employee()
emp1.name = "Rishi"
emp1.age = 7
emp1.salary = 20000

emp1.display()

emp2 = Employee()
emp2.set_data("Jay",5, 15235.10)
emp2.display()
