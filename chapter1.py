# This program says hello and asks for information.

print("Hello!")
print("What's your name:")
name = input()
print("oh wow!", name, "nice to meet you")
print("The lenght of your name is:")
print(len(name))
print("What's your age:")
age = input()
print("You will be", str(int(age) + 1), "in a year.")

# Example
print(float("33.5"), float(10))
print(str(22), str("phai"))
print(int(33.2), int("22"))