class Person:
    def _init_(self, name:str, age:int, ID:int):
        self.name = name
        self.age = age
        self.ID = ID 
class Employee(Person):
    def __init__(self, name:str, age:int, ID:int, dept:str, salary:int, teach_sub:list[str]):
        super()._init_(name, age, ID)      # CALLING PERSON CONSTRUCTOR
        self.dept = dept
        self.salary = salary
        self.teach_sub = teach_sub
    def employee_details(self):
        return f"My name is {self.name} and I am belongs to {self.dept} I can teach {', '.join(self.teach_sub)}"
class Student(Person): 
    def __init__(self, name:str, age:int, ID:int, dept:str):
        super()._init_(name, age, ID)
        self.dept = dept
    def student_details(self):
        return f"My name is {self.name} and I am belongs to {self.dept}"
class University:
    students_table = {}
    employees_table = {}
    def _init_(self, uni_name:str, uni_course:list[str]):
        self.uni_name = uni_name
        self.uni_course = uni_course
    def admission(self, std_obj:Student):
        if std_obj.ID not in self.students_table:
            self.students_table[std_obj.ID] = [std_obj.name, std_obj.age, std_obj.dept]
            return "Student added Successfully"
    def employee_admission(self, emp_obj:Employee):
        # FIX: employees_table, not Employees_table
        if emp_obj.ID not in self.employees_table:
            self.employees_table[emp_obj.ID] = [emp_obj.name, emp_obj.age, emp_obj.dept, emp_obj.salary, emp_obj.teach_sub]
            return "Employee added Successfully"

    def student_details(self, std_ID:int=None, dept:str=None):
        # FIX: students_table, not std_table
        if std_ID:
            return self.students_table.get(std_ID, "Student Not Found")
        elif dept:
            students = []
            for item in self.students_table.items():
                if item[1][2] == dept:
                    students.append((item))
            return students
        if not std_ID and not dept:
            return self.students_table.items()
        else:
            return "Student ID or department not found"
    def employee_details(self, emp_ID:int=None, dept:str=None):
        # FIX: employees_table, not Employees_table
        if emp_ID:
            return self.employees_table.get(emp_ID, "Employee Not Found")
        elif dept:
            employees = []
            for item in self.employees_table.items():
                if item[1][2] == dept:
                    employees.append((item))
            return employees

        if not emp_ID and not dept:
            return self.employees_table.items()

        else:
            return "Employee ID or department not found"

    def total_student_count(self):
        return f"Total students in university is {len(self.students_table)}"

    def total_employee_count(self):
        return f"Total Employees in university is {len(self.employees_table)}"

    def remove_student(self, std_ID:int):
        if std_ID in self.students_table:
            self.students_table.pop(std_ID)
            return "Successfully student removed from university"
        else:
            return "Student id not found"
    def remove_employee(self, emp_id:int):
        if emp_id in self.employees_table:
            self.employees_table.pop(emp_id)
            return "Successfully employee removed from university"
        else:
            return "employee id not found"
#Main Method
if __name__== "__main__":
    uni = University()
    # Creating Students
    s1 = Student("Hasitha", 21, 101, "CSE")
    s2 = Student("Rahul", 22, 102, "ECE")
    s3 = Student("sri", 22, 103, "IT")
    s4 = Student("sai", 23, 104, "ECE")
    s5 = Student("nithin", 23, 105, "CSE")     
    #adding students
    print(uni.admission(s1))
    print(uni.admission(s2))
    print(uni.admission(s3))
    print(uni.admission(s4))
    print(uni.admission(s5))

    # Creating Employees
    e1 = Employee("Mohan", 40, 1201,"CSE", 50000, ["Python","Java","C++"])
    e2 = Employee("Anita", 38, 1202,"ECE", 60000, ["Machine Learning","VLSI","STLD"])
    e3 = Employee("Vidya", 30, 1203, "IT", 80000, ["Java","DBMS","OS"])
    #adding employees  
    print(uni.employee_admission(e1))
    print(uni.employee_admission(e2))
    print(uni.employee_admission(e3))

    
    print(uni.total_employee_count())
    print(uni.total_student_count())
    print(uni.student_details(std_ID=102))
    print(uni.student_details(dept="ECE"))
    print(list(uni.student_details()))
    print(uni.employee_details(emp_ID=1202))
    print(list(uni.employee_details()))
