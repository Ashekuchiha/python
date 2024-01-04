def add(x=0, y=0):
    return print(f"total = {x + y}")


def sub(x=0, y=0):
    return print(f"total = {x - y}")


def mul(x=0, y=0):
    return print(f"total = {x * y}")


def dev(x=0, y=0):
    return print(f"total = {x / y}")


def poww(x=0, y=0):
    return print(f"total = {pow(x,y)}")


def main():
    print("choose your operation \n1.add\n2.subtract\n3.multiply\n4.devide\n5.power")
    choice = input("your choice = ")
    x = int(input("enter first number = "))
    y = int(input("enter second number = "))
    match choice:
        case "1":
            add(x, y)
        case "2":
            sub(x, y)
        case "3":
            mul(x, y)
        case "4":
            dev(x, y)
        case "5":
            poww(x, y)
        case _:
            print("choice something .")


main()
