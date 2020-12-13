# Write your code here

def give_status(state):
    print("The coffee machine has:")
    print("{} of water".format(state.get("water")))
    print("{} of milk".format(state.get("milk")))
    print("{} of coffee beans".format(state.get("beans")))
    print("{} of disposable cups".format(state.get("discups")))
    print("{} of money".format(state.get("money")))
    
    
def buy(state):
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    drink_choice = input()
    state["discups"] = state.get("discups") - 1
    if drink_choice == "1":
        state["water"] = state.get("water") - 250
        state["beans"] = state.get("beans") - 16
        state["money"] = state.get("money") + 4
    elif drink_choice == "2":
        state["water"] = state.get("water") - 350
        state["milk"] = state.get("milk") - 75
        state["beans"] = state.get("beans") - 20
        state["money"] = state.get("money") + 7
    else:
        state["water"] = state.get("water") - 200
        state["milk"] = state.get("milk") - 100
        state["beans"] = state.get("beans") - 12
        state["money"] = state.get("money") + 6
    
        
def fill(state):
    print("Write how many ml of water do you want to add:")
    state["water"] = state.get("water") + int(input())
    print("Write how many ml of milk do you want to add:")
    state["milk"] = state.get("milk") + int(input())
    print("Write how many grams of coffee beans do you want to add:")
    state["beans"] = state.get("beans") + int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    state["discups"] = state.get("discups") + int(input())
    
    
def take(state):
    print("I gave you ${}".format(state.get("money")))
    state["money"] = 0


state = {
    'money' : 550,
    'water' : 400,
    'milk' : 540,
    'beans' : 120,
    'discups' : 9
}
give_status(state)
print("Write action (buy, fill, take):")
choice = input()
if choice == "buy":
    buy(state)
elif choice == "fill":
    fill(state)
else:
    take(state)
give_status(state)

