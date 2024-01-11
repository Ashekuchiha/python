import random

class Company:
    def __init__(self, name, owners):
        self.name = name
        self.owners = owners

    def __str__(self):
        return f"{self.owner()} is the owner of {self.name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("no name")
        self._name = name

    @classmethod
    def owner(cls, propertyName):
        print(f"{random.choice(propertyName.owners)} is the owner {propertyName.name}")


def getOwner():
    owners = []
    ownersNumber = int(input("how many person you want to check = "))
    for i in range(ownersNumber):
        ownersName = input(f"person {i + 1} Name = ")
        owners.append(ownersName)
    return owners


def main():
    owners = getOwner()
    companyName = input("property name = ")
    ownerName = Company(companyName, owners)
    toss = int(input("how many time do you want to check = "))
    for j in range(toss):
        Company.owner(ownerName)

    print("\n which name came more will be the owner ")

if __name__ == '__main__':
    main()
