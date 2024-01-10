
import random
class person :
    names = ["ashik","alif","shakil"]

    @classmethod
     
    def owner(cls):
        print(f"owner is {random.choice(cls.names)}")
person.owner()
p=person()
p.owner()