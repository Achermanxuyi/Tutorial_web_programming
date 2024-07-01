# Hello world 
print("Hello, world!")

print("\n")

# Variables
a = 38 # integer
b = 1.5 # float
c = "Hello!" # str
d = True # bool
e = None # NoneType

print(f"a is a integer: {a}")
print(f"b is a float: {b}")
print(f"c is a str: {c}")
print(f"d is a bool: {d}")
print(f"e is a NoneType: {e}")

print("\n")

# Formatting Strings
name = input("Name: ")
print("Hello " + name)

print("\n")

# Formatted 
print(f"Hello {input('Name: ')}")

print("\n")

# Conditioins
num = int(input("Number: "))
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is 0")

print("\n")

# Sequences
# Strings
name = "Harry"
print(name[0])
print(name[1])

# List
names = ["Harry", "Ron", "Hermione"]
# Print the entire list:
print(names)
# Print the second element of the list:
print(names[1])
# Add a new name to the list:
names.append("Draco")
# Sort the list (in a alphabetical order):
names.sort()
# Print the new list:
print(names)

print("\n")

