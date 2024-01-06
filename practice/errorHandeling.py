def getInt():
    while True:
        try :
            x = int(input("enter the value = "))
            #return int(input("enter the value = ")) #python way
        except ValueError:
            print(  "x is not a integer ")
            #pass #python way
        else:
            break
    return x
def main():
    print(getInt())
    n=getInt()
    print(n)


main()
