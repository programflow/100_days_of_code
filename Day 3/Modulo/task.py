#The result for the print statement should be 1
from math import remainder

print(10 % 3)

number = int(input("Choose an in integer: "))
if (number % 2 ) == 0:
    print("The number is even.")
else:
    print("The number is odd.")