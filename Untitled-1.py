class employee:
    def __init__(self,empid,name,age,salary):
        self.empid=empid
        self.name=name
        self.age=age
        self.salary=salary
class empd:
    def __init__(self):
        self.employees=[]
    def add(self,emp):
        self.employees.append(emp)
    def search_a(self,age):
        find=[emp for emp in self.employees if emp.age == age]
        return find
    def search_n(self,name):
        find=[emp for emp in self.employees if emp.name.lower() == name.lower()]
        return find
    def search_s(self,operator,salary):
        if operator=='>':
            find=[emp for emp in self.employees if emp.salary>salary]
        elif operator=='<':
            find=[emp for emp in self.employees if emp.salary<salary]
        elif operator=='>=':
            find=[emp for emp in self.employees if emp.salary>=salary]
        elif operator=='<=':
            find=[emp for emp in self.employees if emp.salary<=salary]
        else:
            find=[]
        return find
    def display(self,finds):
        if not finds:
            print("Record not found!! Please try again or enter a different value!")
        else:
            for emp in finds:
                print(f"Employee ID: {emp.empid}, Name: {emp.name}, Salary: {emp.salary}")
def main():
    db=empd()
    db.add(employee("161E90", "Raman", 41, 56000))
    db.add(employee("161F91", "Himadri", 38, 67500))
    db.add(employee("161F99", "Jaya", 51, 82100))
    db.add(employee("171E20", "Tejas", 30, 55000))
    db.add(employee("171G30", "Ajay", 45, 44000))
    print("Which option would you like to choose:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    ch=input("Choose among 1,2 or 3: ")
    if ch=='1':
        age=int(input("Enter the age: "))
        finds=db.search_a(age)
    elif ch=='2':
        name=input("Enter the name: ")
        finds=db.search_n(name)
    elif ch=='3':
        operator = input("Enter operator (> / < / >= / <=): ")
        salary=int(input("Enter the salary: "))
        finds=db.search_s(operator,salary)
    else:
        print("Invalid choice!!")
        return
    db.display(finds)
if __name__== "__main__":
    main()