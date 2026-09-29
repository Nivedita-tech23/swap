a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print("Addition =",a + b)
print("Subraction =",a - b)
print("Multiplication =",a * b)

if b != 0:
    print("Division =",a / b)
else:
    print("Division is not possible because denominator is zero.")