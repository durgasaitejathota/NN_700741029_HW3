class Employee:
    count = 0

    def __init__(self, name, family_name, salary, dpt):
        self.__name = name
        self.__family_name = family_name
        self.salary = salary
        self.__dpt = dpt
        Employee.count += 1

    def average_salary(employees):
        sum = 0
        for employee in employees:
            sum += employee.salary
        return sum / Employee.count
class FulltimeEmployee(Employee):
    def __init__(self, name, family_name, salary, dpt):
        super().__init__(name, family_name, salary, dpt)

def main():
    employees = []
    fte1 = FulltimeEmployee("durga", "thota", 1200000, "Unknown")
    employees.append(fte1)
    fte2 = FulltimeEmployee("akash", "varri", 1800000, "US")
    employees.append(fte2)
    emp1 = Employee("guru", "gum", 1600000, "Sales")
    employees.append(emp1)
    emp2 = Employee("banti", "bs", 135000, "UK")
    employees.append(emp2)
    print("Average salary:", FulltimeEmployee.average_salary(employees))


if __name__ == "__main__":
    main()