class Company:
    def __init__(self, name, city, mobile_no):
        self.name = name
        self.city = city
        self.mobile_no = mobile_no

    def display_company_details(self):
        print(f"Company Name: {self.name}")
        print(f"City: {self.city}")
        print(f"Mobile No: {self.mobile_no}")

class Employee(Company):
    def __init__(self, name, city, mobile_no, emp_name,  designation, salary):
         super().__init__(name, city, mobile_no)
         self.emp_name = emp_name
         self.designation = designation
         self.salary = salary

    def display_employee_details(self):
          self.display_company_details()
          print(f"Employee Name: {self.emp_name}")
          print(f"Designation: {self.designation}")
          print(f"Salary: {self.salary}")

# Create an Employee object
employee1 = Employee("Tech Corp", "New York", "1234567890", "John Doe", "Software Engineer", 70000)

# Display the details of the employee
employee1.display_employee_details()


