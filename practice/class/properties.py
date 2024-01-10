
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, you are {self.age} year's old"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if  not age:
            raise ValueError("not shakil")
        self._age = age

def getInfo():
    name = input("name = ")
    age = int(input("age = "))
    return Person(name, age)

def main():
    shakil = getInfo()
    shakil.age=8
    print(shakil)


if __name__ == "__main__":
    main()
