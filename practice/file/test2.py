#
# #normally creat a file and write text
# file1 = open("test1.txt", "w")
# file1.write(input("what is your name ="))
# file1.close()
# #normally write multiple
# file2 = open("test2.txt","w")
# for _ in range(3) :
#     file2.write(f"{input('write your name = ')} \n")
# file2.close()
#
# file3 = open("test3.txt", "a")
# file3.write(f"{input('write your name = ')} \n")
# file3.close()
#
# file4 = open("test4.txt","a")
# for _ in range(3) :
#     file4.write(f"{input('write your name = ')} \n")
# file4.close()

#read it 3 ways and show
reading = open("test4.txt","r")
lines = reading.readlines()
for line in lines :
    print("hi , ",line)
for words in lines :
    print("hi , ",words,end="")
for word in lines :
    print("hi , ",word.rstrip())

#read it and save it in list and show
lists = []
for word in lines :
    lists.append(word.rstrip())
print(lists)

