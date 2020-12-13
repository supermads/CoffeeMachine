# Write your code here
class CoffeeMachine:
    def __init__(self, water, milk, beans, discups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.discups = discups
        self.money = money
    
    
    def give_status(self):
        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.beans))
        print("{} of disposable cups".format(self.discups))
        print("{} of money".format(self.money))
    
    
    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        drink_choice = input()
        if self.discups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            if drink_choice == "1":
                if self.water >= 250 and self.beans >= 16:
                    print("I have enough resources, making you a coffee!")
                    self.discups -= 1
                    self.water -= 250
                    self.beans -= 16
                    self.money += 4
                else:
                    if water < 250:
                        print("Sorry, not enough water!")
                    else:
                        print("Sorry, not enough coffee beans!")
            elif drink_choice == "2":
                if self.water >= 350 and self.beans >= 20 and self.milk >= 75:
                    print("I have enough resources, making you a coffee!")
                    self.discups -= 1
                    self.water -= 350
                    self.milk -= 75
                    self.beans -= 20
                    self.money += 7
                else:
                    if self.water < 350:
                        print("Sorry, not enough water!")
                    elif self.milk < 75:
                        print("Sorry, not enough water!")
                    else:
                        print("Sorry, not enough coffee beans!")
            elif drink_choice == "3":
                if self.water >= 200 and self.milk >= 100 and self.beans >= 12:
                    print("I have enough resources, making you a coffee!")
                    self.discups -= 1
                    self.water -= 200
                    self.milk -= 100
                    self.beans -= 12
                    self.money += 6
                else:
                    if self.water < 200:
                        print("Sorry, not enough water!")
                    elif self.milk < 100:
                        print("Sorry, not enough water!")
                    else:
                        print("Sorry, not enough coffee beans!")
    
        
    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.discups += int(input())
    
    
    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0


    def menu(self, keep_running):   
        while keep_running:
            print("Write action (buy, fill, take, remaining, exit):")
            choice = input()
            if choice == "buy":
                self.buy()
            elif choice == "fill":
                self.fill()
            elif choice == "take":
                self.take()
            elif choice == "remaining":
                self.give_status()
            else:
                keep_running = False
        
        
keep_running = True
coffee = CoffeeMachine(water = 400, milk = 540, beans = 120, discups = 9, money = 550)
coffee.menu(keep_running)
