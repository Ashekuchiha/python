name = input("what is your full name ? \n ").strip().title()
firstName, lastName = name.split(" ")
age = input("how old are you ? \n").strip().title()
print(f"hi {firstName} you are {age} years old \n")
