print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
#todo: work out how muc they need to pay based on their size choice.
if size.upper() == "S":
    bill += 15
elif size.upper() == "M":
    bill += 20

elif size.upper() == "L":
    bill += 25

else:
    exit()
if pepperoni.upper() == "Y":
    bill += 3

if extra_cheese.upper() == "Y":
    bill += 1


print(f"Your final bill is: ${bill}.")


#todo: work out how much to add to their bill based on their pepperoni choice.

#todo: wor out their final amount based on whether if they want extra cheese.