# Write your code here
print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
beans = int(input())
print("Write how many cups of coffee you will need:")
cups = int(input())
cups_available = 0
while water >= 200 and milk >= 50 and beans >= 15:
    cups_available += 1
    water = water - 200
    milk = milk - 50
    beans = beans - 15
if cups == cups_available:
    print("Yes, I can make that amount of coffee")
elif cups_available > cups:
    extra = cups_available - cups
    print("Yes, I can make that amount of coffee (and even {} more than that)".format(extra))
else:
    print("No, I can make only {} cups of coffee".format(cups_available))
    
    
