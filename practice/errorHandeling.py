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

def getInfo():
    name = input("NAME = ")
    age = int(input("AGE = "))
    if name not in ["ashik","alif","shakil","sharmin"] :
        raise ValueError("enter valid name") #ei error ami nijy banaici
    return  print(f"{name} is {age} years old")
def main():
    print(getInt())
    n=getInt()
    print(n)
    try :
        getInfo()
    except ValueError : # try korar por jodi vhul pai taholy prog crash korby na except e choly asby
        print("dont find the name")

    getInfo() #getINfo() try except chara use kori taholy valuerror amar ta raise korby and prog crash korby


main()
