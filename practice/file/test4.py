
# with open("test6.csv","a") as book :
#     for _ in range(3):
#         book.write(f"{input('what is your name = ')},{int(input('how much you earn = '))}\n")


with open("test6.csv") as book :
    lines = book.readlines()
    for line in sorted(lines) :
        words = line.rstrip().split(",")
        name,income = line.split(",")
        print(f"{words[0]} income is {words[1]}")
        print(f"{name} income is {income}")