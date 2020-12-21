number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

print("Choices are:")
print("1 - Add")
print("2 - Subtract")
print("3 - Divide")
print("4 - Multiply")
operation = int(input("Enter choice: "))

if operation == 1:
    print(f"{number1} + {number2} = {number1 + number2}")
elif operation == 2:
    print(f"{number1} - {number2} = {number1 - number2}")
elif operation == 3:
    print(f"{number1} / {number2} = {number1 / number2}")
elif operation == 4:
    print(f"{number1} * {number2} = {number1 * number2}")
else:
    print(f"operation {operation} not supported")