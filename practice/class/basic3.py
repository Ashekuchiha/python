class Person :
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name} u r {self.age} years old and ur income is {self.income()}"

    def income (self) :
        match self.name :
            case "ashik" :
                return 0
            case "shakil" :
                return 100000
            case _:
                return "shafiq"

def main() :
    person = Person("ashik",20)
    print(person)
    x=person.income()
    print(x)

if __name__ == '__main__':
    main()
