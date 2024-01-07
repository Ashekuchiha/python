
# with open("infos.csv.txt","a") as book :
#     for i in range(3):
#         book.write(f"{input(f'Student {i+1} write your name = ')},{int(input(f'STydent {i+1} write your age = '))}\n")

students = []
with open("test6.csv") as book :
    line = book.readlines()#info.csv file er line gula anlam list kory
    print(line)#info.csv file e jmon chilo list er moto
    for word in line :
        #print(word)#list thika read kory word by word anlam
        print(word.rstrip())#.rstrip() use kory extra line bad dilam
        name,age=word.rstrip().split(",")# , dia 2 ta vag korlam ashik,0 thika ashik k dilam name e and o dilam age e
        student={"name":name,"age":age}#eibar name key ty name age key ty age raklam and list banailam
        students.append(student)#list gula nia diction arry banailam
print(student)
print(f"it is a dictionary : {students}")
for student in students :
    print(student["name"],student["age"])#dictionary thika abr print korlam

