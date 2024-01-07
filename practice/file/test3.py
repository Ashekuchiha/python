
lists=[]

# with open("test5.txt","a") as book :
#     for _ in range(3):
#         book.write(f"{input('write your name = ')} \n")

with open("test5.txt","r") as book :
    line = book.readlines()
    for word in line :
        print("hi, ",word,end="")
        lists.append(word.rstrip())

print(lists)
print(sorted(lists))

with open("test5.txt") as book2 :
    for line in sorted(book2) :
        print("hi, ",line.rstrip())