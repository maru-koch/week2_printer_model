
from data.data import FORMAT, resources, coins
import time


class Printer():
    power = True
    def __init__(self,paper,ink,profit):
        self.paper = paper
        self.ink = ink
        self.profit = profit
        self.coin = ''
        self.pages = 0
        self.mode = ''
        self.number = 0
        
        self.amount = 0
        self.ink_consumable = 0
        self.cost = 0


    
    def off(self):
        print("TURNING OFF...")
        time.sleep(1)
        self.power = False
        print("BYE..")

    def report(self):
        report = f"Paper: {self.paper} Pc \nInk: {self.ink} ml \nProfit: ${self.profit}"
        print(report)

    def checkAvailableResources(self, mode, pages):
        available_ink = self.ink
        avalaible_paper = self.paper
        ink = FORMAT[self.mode]['materials']['ink']

        self.ink_consumable = ink * pages

        if pages > avalaible_paper:
            print ("Insufficient Paper")

        elif self.ink_consumable > available_ink:
            print ("Insufficient Ink")

        else:
            return True
    

    def printDocument(self):
        "Printing Document ... "
        time.sleep(1)
        print("-----------------")
        print("REPORT -- BEFORE")
        report = self.report()
        print(report)

        print("-----------------")
        self.processDocument()
        self.printing()

        print("-----------------")
        print("REPORT -- AFTER")
        report = self.report()
        print(report)
        
        if self.amount > self.cost:
            balance = self.check_balance(self.amount, self.cost)
            print(balance)
        
        thanks = self.exitMsg()
        print(thanks)

    def processDocument(self):
        self.ink -= self.ink_consumable 
        self.paper -= self.pages
        self.profit += self.cost

        
    def printing(self):
        pages = self.pages
        printed = pages
        i = 1
        while pages:
            timeformat = '{:2d}'.format(pages)
            print("|"*i, "\tPrinting... ", timeformat, end='\r')
            time.sleep(0.2)
            pages -= 1
            i += 1
        print(f"\n{printed} pages Printed")

    def check_balance(self, amount, cost):
        return f"Here is ${amount - cost} in change"

    def exitMsg(self):
        return "\nHere is your Project. Thank you for using our services\n"

class Cost(Printer):
    
    def displayCost(self):
        """
            - displays the printing cost
        """
        price = self.price = FORMAT[self.mode]['price']
        cost =  price * self.pages
        print(f" \n\t    MODE: {self.mode}  \n\t    PAGES: {self.pages} \n\t    COST: ${cost}")
    
    def add_fund(self):
        valid = False
        while not valid:
            self.coin = input(f"remaining ${self.cost - self.amount}, Please Insert More coins... (Penny, Nickel, Dime, or Quarter): ")
            self.number = int(input("Enter Number of coins: "))
            self.amount += coins[self.coin] * self.number
            if self.amount >= self.cost:
                valid = True
        else:
            self.printDocument()
        
    def check_balance(self, amountEntered, cost):
        balance = amountEntered - cost
        if balance:
            return f"Here is ${balance} in change"
    
    def estimate_profit(self, price: int) -> int:
        self.profit += price
        
    def processPrice(self) -> int:
        self.cost = FORMAT[self.mode]['price'] * self.pages
        self.amount = coins[self.coin] * self.number
        return self.cost, self.amount

    def checkTransaction(self, cost, amountEntered):
        if amountEntered >= cost:
            self.printDocument()
        else:
            return input(f"Insufficient Fund: ${self.amount}. Would like to add more fund? y/n   ")



class Print(Cost):
    def requestUserInput(self):
        response = input("What format would you like? greyscale or coloured: ")
        return response
    
    def processResponse(self, response):
        self.mode = response
        self.pages = int(input("How many pages would you like to print: "))

        # check if there are enough ink and paper
        isResourceAvailable = self.checkAvailableResources(self.mode, self.pages)
        if isResourceAvailable:
            self.displayCost()
            response = input("Proceed? y/n  ")
            if response == 'y':
                coin = input("Please Insert coin... (Penny, Nickel, Dime, or Quarter): ")
                self.coin = coin.lower()
                self.number = int(input("Enter Number of coins: "))

                #: check if fund entered by user is sufficient
                #: if it is, print document -> called in checkTransaction method

                cost, amountEntered = self.processPrice()
                response = self.checkTransaction(cost, amountEntered)
        
                if response == 'y':

                    self.add_fund()
                
                else:
                    self.requestUserInput()
            else:
                self.requestUserInput()
               




