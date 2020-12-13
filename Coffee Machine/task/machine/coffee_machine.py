# Write your code here

def give_status(state):
    print("The coffee machine has:")
    print("{} of water".format(state.get("water")))
    print("{} of milk".format(state.get("milk")))
    print("{} of coffee beans".format(state.get("beans")))
    print("{} of disposable cups".format(state.get("discups")))
    print("{} of money".format(state.get("money")))
    
    
def buy(state):
    d = state.get("discups")
    w = state.get("water")
    m = state.get("milk")
    b = state.get("beans")
    mo = state.get("money")
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    drink_choice = input()
    if d < 1:
        print("Sorry, not enough disposable cups!")
    else:
        if drink_choice == "1":
            if w >= 250 and b >= 16:
                print("I have enough resources, making you a coffee!")
                state["discups"] = d - 1
                state["water"] = w - 250
                state["beans"] = b - 16
                state["money"] = mo + 4
            else:
                if w < 250:
                    print("Sorry, not enough water!")
                else:
                    print("Sorry, not enough coffee beans!")
        elif drink_choice == "2":
            if w >= 350 and b >= 20 and m >= 75:
                print("I have enough resources, making you a coffee!")
                state["discups"] = d - 1
                state["water"] = w - 350
                state["milk"] = m - 75
                state["beans"] = b - 20
                state["money"] = mo + 7
            else:
                if w < 350:
                    print("Sorry, not enough water!")
                elif m < 75:
                    print("Sorry, not enough water!")
                else:
                    print("Sorry, not enough coffee beans!")
        elif drink_choice == "3":
            if w >= 200 and m >= 100 and b >= 12:
                print("I have enough resources, making you a coffee!")
                state["discups"] = d - 1
                state["water"] = w - 200
                state["milk"] = m - 100
                state["beans"] = b - 12
                state["money"] = mo + 6
            else:
                if w < 200:
                    print("Sorry, not enough water!")
                elif m < 100:
                    print("Sorry, not enough water!")
                else:
                    print("Sorry, not enough coffee beans!")
    
        
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


def menu(state, keep_running):   
    while keep_running:
        print("Write action (buy, fill, take, remaining, exit):")
        choice = input()
        if choice == "buy":
            buy(state)
        elif choice == "fill":
            fill(state)
        elif choice == "take":
            take(state)
        elif choice == "remaining":
            give_status(state)
        else:
            keep_running = False
        
        
state = {
    'money' : 550,
    'water' : 400,
    'milk' : 540,
    'beans' : 120,
    'discups' : 9
}
keep_running = True
menu(state, keep_running)


