def loop1():
    while True:
        n = int(input("how many = "))
        if n < 0:
            continue
        else:
            break
    while True:
        a = int(input("how many s= "))
        if a >= 0:
            break

    i = 0
    while i < 3:
        print("hi")
        i += 1


def loop2():
    for i in ["ashik", "alif", "shakil", "sharmin"]:
        print(i)

    for _ in range(5):
        print("you are bolod ")

    for i in range(3):
        print(f"{i}.bolod")


def main():
    # loop1()
    loop2()
    print("x\n" * 3, end="")



main()
