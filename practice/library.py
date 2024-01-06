from random import choice, randint
import statistics
import sys

i = 0
while i <= 1:
    coin = choice(["head", "tail"])
    you = input("head or tail = ")
    if coin == "head":
        print("pass")
    else:
        print("fail")
    i += 1

j = 0
while j <= 3:
    n = randint(1, 5)
    print(n)
    j += 1

print(f"mean is = {statistics.mean([2, 2])}")
if len(sys.argv) == 1:
    sys.exit("need name")
else:
    print(f"this name come from terminal = {sys.argv[1]}")
