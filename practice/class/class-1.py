import random


class Company:
    owners = ["ashik", "alif", "shakil"]

    @classmethod
    def get(cls):
        name = input("company name = ")
        return cls(name)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        # return f"my name is {self.name} "
        return f"{random.choice(self.owners)} is the owner of {self.name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("no name")
        self._name = name

    @classmethod
    def owner(cls, ownerName):
        print(f"{random.choice(cls.owners)} is the owner of {ownerName.name}")


def main():
    companyName = input("which company = ")
    ownerName = Company(companyName)
    Company.owner(ownerName)  # it call by classmethod
    # print(ownerName)#it call by __str__


if __name__ == '__main__':
    main()
