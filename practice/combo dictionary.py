infos = [
    {"name":"ashak ul islam","age":24},
    {"name":"alif","age":22}
]
print(infos)
for info in infos :
    print(info)
print("\n\n")

for info in infos :
    print(info["name"])
print("\n\n")

for info in infos :
    for about in info :
        print(about)
print("\n\n")

for info in infos :
    for about in info :
        print(about,info[about],sep="=")
print("\n\n")