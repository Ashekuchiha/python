
import random

class Company:
    #owners = ["ashik","alif","shakil"]
    @classmethod
    def get(cls):
        name = input("company name = ")
        return cls(name)

    def __init__(self, name,owners):
        self.name = name
        self.owners= owners

    def __str__(self):
        #return f"my name is {self.name} "
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
    def owner(cls,ownerName):
        print(f"{random.choice(ownerName.owners)} love with you {ownerName.name}")

def getOwner():
    owners=[]
    ownersNumber=int(input("how many person you want to check = "))
    for i in range(ownersNumber) :
        ownersName=input(f"person {i+1} Name = ")
        owners.append(ownersName)
    return owners
def main():
    owners=getOwner()
    companyName=input("Enter your name = ")
    ownerName = Company(companyName,owners)
    toss=int(input("how many time do you want to check = "))
    for _ in range(toss) :
        Company.owner(ownerName)
    print("\n which name came more will be the perfect life pertner for you ")
    print("\n let give it a try")
    print("\n by the way owner of this programmer will be your best choice \U0001F603")


if __name__ == '__main__':
    main()