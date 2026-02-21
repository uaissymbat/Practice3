class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def total_salary(self):
        return self.base_salary

class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent

    def total_salary(self):
        return self.base_salary * (1 + self.bonus_percent / 100)

class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects

    def total_salary(self):
        return self.base_salary + self.completed_projects * 500

class Intern(Employee):
    pass

# Read input
line = input().split()
emp_type = line[0]
name = line[1]

if emp_type == "Manager":
    base = int(line[2])
    bonus = int(line[3])
    emp = Manager(name, base, bonus)
elif emp_type == "Developer":
    base = int(line[2])
    projects = int(line[3])
    emp = Developer(name, base, projects)
else:  # Intern
    base = int(line[2])
    emp = Intern(name, base)

total = emp.total_salary()
print(f"Name: {name}, Total: {total:.2f}")
