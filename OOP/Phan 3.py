from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def salary_calculation(self):
        pass

class FullTime(Employee):
    def __init__(self, salary, workDays):
        self.salary = salary
        self.workDays = workDays
    def salary_calculation(self):
        return f"Luong FullTime: {self.salary * self.workDays}"

class PartTime(Employee):
    def __init__(self, working_hours, salary_by_hour):
        self.working_hours = working_hours
        self.salary_by_hour = salary_by_hour
    def salary_calculation(self):
        return f"Luong PartTime: {self.working_hours * self.salary_by_hour}"

emp1 = FullTime(120, 5)
emp2 = PartTime(123, 123)

def print_employee(employee):
    print(employee.salary_calculation())

print_employee(emp1)
print_employee(emp2)