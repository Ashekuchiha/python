import csv
name = input("name = ")
salary = int(input("salary = "))
with open("text2.csv", "a") as book:
    writer = csv.DictWriter(book, fieldnames=["name", "salary"])
    writer.writerow({"salary": salary, "name": name})
