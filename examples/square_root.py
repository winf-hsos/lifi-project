import sys
print("I can calculate square roots!")

number = input("A number, please: ")
number = int(number)

if number < 0:
    sys.exit()

a = number / 2
b = number / a

while(abs(a - b) > 0.00001):
    a = (a + b) / 2
    b = number / a

print(f"The square root of { number } is { a }")
