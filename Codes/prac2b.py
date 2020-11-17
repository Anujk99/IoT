# Read the two numbers and print their sum, difference, product and division

import sys

if len(sys.argv) != 3:
    print("Give two number as an argument")
    sys.exit()

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
except ValueError:
    print("Enter only number as argument")

summ = a + b
print(f"Sum of two number is: {summ}")
diff = a - b
print(f"Difference of two number is: {diff}")
prod = a*b
print(f"Product of given two number is: {prod}")

try:
    div = a/b
    print(f"Divison of given two number is: {div}")
except ZeroDivisionError:
    print("Second argument must be non zero for division")
