class Employee:
    def __init__(self, name, date_of_join, designation, salary):
        self.name = name
        self.date_of_join = date_of_join
        self.designation = designation
        self.salary = salary

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Date of Joining: {self.date_of_join}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary}")

# Create an Employee object
employee1 = Employee("John Doe", "2021-07-30", "Software Engineer", 70000)

# Display the details of the employee
employee1.display_details()

