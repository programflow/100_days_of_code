print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_decimal = tip/100
total_bill = bill*(1+ tip_decimal)
split_cost = round(total_bill/float(people), 2)
print(f"Each person should pay: ${split_cost}")


