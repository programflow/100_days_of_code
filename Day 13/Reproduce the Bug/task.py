from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]

# problem with current code is that randint is picking numbers
# to place inside the index of dice_images and six is not a position in
# the list since counting starts at 0 for indices
# dice_num = randint(1, 6)
# print(dice_images[dice_num])

dice_num = randint(0, 5)
print(dice_images[dice_num])

