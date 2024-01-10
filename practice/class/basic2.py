class Person:
    def __init__(self, name="shafiq", age=75):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, you are {self.age} year's old"

def getInfo():
    name = input("name = ")
    age = int(input("age = "))
    return Person(name, age) #creat obj of person

def main():
    shakil = getInfo()
    #shakil.age=3 #for prevent this go properties.py
    print(shakil)


if __name__ == "__main__":
    main()
