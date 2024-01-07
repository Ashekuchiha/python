students = []
with open("test6.csv") as book :
    line = book.readlines()
    for word in line :
        name,age=word.rstrip().split(",")
        student={"name":name,"age":age}
        students.append(student)

# def getKey(x,y):callback or arrow function
#     print(x[y])
#     return x[y]
# getKey(student,"name")
def getName (student):
    print(student["name"])
    return student["name"]

for student in sorted(students,key=getName,reverse=True) :
    print(f"{student['name']} is {student['age']} years old")

for student in sorted(students,key=lambda getname : student["name"],reverse=True) :
    print(f"{student['name']} is {student['age']} years old")

for student in sorted(students,key=lambda getname : student["name"],reverse=True) :
    print(f"{student['name']} is {student['age']} years old")