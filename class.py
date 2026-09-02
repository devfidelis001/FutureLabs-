


class management:
    def __init__(self, name, attendance, time, phone_number, skill, bill):
        
        self.names = []
        self.attend = []
        self.time = time
        self.number = phone_number
        self.skills = skill
        self.debt = bill
        
        self.names.append(name)
        self.attend.append(attendance)
        self.attended = len(self.attend)
            
        
        
    def show(self):
        print(f"""student names: {self.names}
                  total present: {self.attended}
                  time for student attended: {self.time}
                  phone number: {self.number}
                  skills : {self.skills}
                  amount of student owing: {self.debt}
                       
              """)
name = input("student name>>")
inclass = input("student active status>>")
time = input("student participation time>>")
num = input("student phone no>>")
taent = input("student skill>>")
owe = input("student owing status>>")


display = management(name, inclass, time, num, taent, owe)
print(display.show())




class name:
    def __init__(self, name, age, ):
        self.name = name
        self.age = age
    def show(self):
        print(f"thats all for {self.name}")
class display(name):
    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.num = number
        print(f"{self.name}, {self.age}, {self.num}")
        

showme = name("me ", 10)
info = display("you")
display.show





