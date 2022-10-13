print("Put your name: ")
name = input()
print("Put your surname: ")
surname = input()
print("Put your Birth date: ")
year = input()

print(name, "_", surname, "_", year)

c = name
name = surname
surname = c
year = int(year) + 60

print(name, "_", surname, "_", year)