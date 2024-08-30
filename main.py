from Auction import logo
from replit import clear
user_input: str = "yes"
print(logo)

# Initialize dictionary
user_dict = {}

# Function to find the highest bid
def find_highest_bid(bid_record):
    highest_bidder = max(bid_record, key=bid_record.get)
    highest_bid = bid_record[highest_bidder]
    return highest_bidder, highest_bid

num_entries = int(input("\nEnter the number of entries you want to add: "))
# Main auction logic
while user_input == "yes":
  for i in range(num_entries):
    key = input("\nEnter your name: ")
    value = int(input("Enter your bid:$ "))
    user_dict[key] = value
    clear()
    print(logo)
    print("Members and and their Bids:", user_dict)
  user_input=input("Do you want to bid again?")

# Determine and display the winner and the highest bid
winner, highest_bid = find_highest_bid(user_dict)
print(f"\nThe winner is {winner} with a bid of ${highest_bid}")