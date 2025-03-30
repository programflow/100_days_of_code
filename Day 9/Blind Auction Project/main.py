import art

print(art.logo)
print("Welcome to the secret auction program.")
bids = {}
keep_bidding = "yes"

while keep_bidding == "yes":
    bidder = input("What is your name?: ")
    bid = input("What's Your bid?: $")

    bids[bidder] = int(bid)

    keep_bidding = input("Are there any other bidders? Type 'yes' or 'no'.")


highest_bid =0
highest_bidder = None

for name in bids:

    if bids[name] > highest_bid:
        highest_bid = bids[name]
        highest_bidder = name

print(f"The winner is {highest_bidder} with a d bid of ${highest_bid}")



