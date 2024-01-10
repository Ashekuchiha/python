import  csv

students=[]

with open("text1.csv") as book :
    reader = csv.DictReader(book)
    for read in reader :
        students.append({"name" : read["name"] , "age":read["age"]})

for student in sorted(students,key=lambda student : student["name"],reverse=False) :
    print(f"{student['name']} is {student['age']} years old")

print(type(student))
print(student)
print(type(students))
print(students)