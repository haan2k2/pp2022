# PhamHungAnhBI11-031
class Student:
    # Constructor
    def __init__(self, name, course, m1, id):
        self.name = name
        self.course = course
        self.m1 = m1
        self.id = id

    # Function to create and append new student
    def accept(self, Name, course, marks1, id):
        # use ' int(input()) ' method to take input from user
        ob = Student(Name, course, marks1, id)
        ls.append(ob)

    # Function to display student details
    def display(self, ob):
        print("Name : ", ob.name)
        print("Course : ", ob.course)
        print("Marks1 : ", ob.m1)
        print("Id : ", ob.id)
        print("\n")

    # Search Function
    def search(self, cr):
        for i in range(ls.__len__()):
            if (ls[i].course == cr):
                return i

    # Delete Function
    def delete(self, cr):
        i = obj.search(cr)
        del ls[i]

    # Update Function
    def update(self, cr, No):
        i = obj.search(cr)
        course = No
        ls[i].course = course;


# Create a list to add Students
ls = []
# an object of Student class
obj = Student('', 0, 0, 0)

print("Hello, Teacher ")
print("There are 3 students in small class")
print("Course 1 : Math")
print("Course 2 : PE")
print("Course 3 : Physics")

# ch = int(input("Enter choice:"))
# if(ch == 1):
obj.accept("A", 1, 100, 100)
obj.accept("B", 2, 90, 90)
obj.accept("C", 3, 80, 80)

# elif(ch == 2):
print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
    obj.display(ls[i])

# elif(ch == 3):
print("\n Student Found, ")
s = obj.search(2)
obj.display(ls[s])

# elif(ch == 4):
obj.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
    obj.display(ls[i])

# elif(ch == 5):
obj.update(3, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):
    obj.display(ls[i])

# else:
print("Thank You !")