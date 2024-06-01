import os
print("*****Welcome to the Silent Auction Program*****")
def find_winner(bidder_details):
    highest_bid=0
    for bidder in bidder_details:
        bidder_price=bidder_details[bidder]
        if bidder_price>highest_bid:
            highest_bid=bidder_price
            winner=bidder
    print(bidder_details)
    print(f"The winner is {winner} with a bid price of {highest_bid}")

bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input("What is your name?: ")
    price=int(input("What is your bid?: "))
    bidder_data[name]=price
    more_bidders=input("Are there any more bidders? Type 'yes or 'no' : ").lower()
    if more_bidders=='no':
        end_of_bidding=True
        os.system('cls')
        find_winner(bidder_data)
    elif more_bidders=='yes':
        os.system('cls')
    
