class Student :
    ...

def getStudent() :
    ...
    student = Student()
    student.name=input("name pls = ")
    student.age=input("age pls = ")
    return  student

def main() :
    ...
    student=getStudent()
    print(f"my name is {student.name} and i am {student.age} years old ")



if __name__ == "__main__" :
    main()