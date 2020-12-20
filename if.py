x = int(input("Enter a number"))

if x < 6:
    print(f"{x} is between 3 and 6")
    print("part of if")
elif 7 <= x << 100:
    print(f"{x} is between 7 and 100")
    print("part of else if")
else:
    print(f"{x} is greater than 100")
    print("part of else")

isEven = True if x % 2 == 0 else False
print(f"isEven={isEven}")
