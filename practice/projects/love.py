import random

boyfriendNumber = int(input("how many boyfriend = "))
boyfriendNames=[]
winers=[]
for i in range(boyfriendNumber) :
    boyfriendName = input(f"boyfriend name {i+1} = ")
    boyfriendNames.append(boyfriendName)

goldDeggerName = input("what is your name = ")
toss = int(input("how many time do u check "))
for j in range(toss):
    winer = random.choice(boyfriendNames)
    winers.append(winer)

occurrences = {winer: winers.count(winer) for winer in winers}
for winer, count in occurrences.items():
    print(f"{winer} get {count} point ")

luckyboyfriend = max(occurrences, key=occurrences.get)

print(f"\t\tCONGRETULATION {goldDeggerName}")
print(f"\t{luckyboyfriend.upper()} will be your date")
print("\t let's give it a try")
print("\n by the way owner of this programmer will be your best choice pk\U0001F603")
print("\n oh, you are a gold degger \U0001F603")


