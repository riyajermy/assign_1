num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = int(num1 + num2)
subtraction = int(num1 - num2)
multiplication = int(num1 * num2)

if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
