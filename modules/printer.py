
from data.data import FORMAT, resources, coins
import time

class Printer(object):
    coin = ''
    pages = 0
    mode = ''
    number = 0
    ink_consumable = 0
    cost = 0
    ink = resources['ink']
    paper = resources['paper']
    profit = resources['profit']

    # def __init__(self):
    #     self.ink = resources['ink']
    #     self.paper = resources['paper']
    #     self.profit = resources['profit']

    def start(self):
        try:
            self.mode = input("What format would you like? greyscale or coloured: ")
            self.pages = int(input("How many pages would like to print: "))
            cost = FORMAT[self.mode]['price'] * self.pages
            print(f" \n\t    MODE: {self.mode}  \n\t    PAGES: {self.pages} \n\t    COST: ${cost}")
            isResource = Printer.checkAvailableResources(self, self.mode, self.pages)
            if isResource:
                response = input("Proceed? y/n  ")
                if response == 'y':
                    self.coin = input("Please Insert coin... (Penny, Nickel, Dime, or Quarter): ").islower()
                    self.number = int(input("Enter Number of coins: "))
                else:
                    self.start()
            else:
                "Insufficient Ink or Paper"

        except ValueError:
            print('Incorrect Value')

        
    def checkMode(self, mode):
        if mode == 'coloured':
            print_format = FORMAT['coloured']
        elif mode == 'greyscaled':
            print_format = FORMAT['greyscaled']
        return print_format

    def printDocument(self):
        self.processDocument(Printer)
        self.printing(Printer)
       
    def displayCost(self):
        cost = FORMAT[self.mode]['price'] * self.pages
        print(f" \n\t    MODE: {self.mode}  \n\t    PAGES: {self.pages} \n\t    COST: ${cost} ")
        

    def processDocument(self):
        self.ink - self.ink_consumable 
        self.paper - self.pages
        self.profit += self.cost

    # def rejectDocument():
    #     print("Document rejected")


    def processPrice(self) -> int:
        cost = FORMAT[self.mode]['price'] * self.pages
        print(self.coin)
        amountEntered = coins['dime'] * self.number
        self.cost = cost
        return cost, amountEntered

    def checkTransaction(self, cost, amountEntered):
        if cost > amountEntered:
            return "Insufficient funds"
        elif amountEntered == cost:
            return True
        else:
            print(Printer.balance(amountEntered, cost))
            return True

    def balance(amountEntered, cost):
        balance = amountEntered - cost
        return f"Here is ${balance} in change"

    def checkAvailableResources(self, mode, pages):
        """
            - Check if there is sufficient amount of ink and paper
            - if not raise error
        """
        available_ink = self.ink
        avalaible_paper = self.paper
        ink = FORMAT[mode]['materials']['ink'] * pages
        if ink > available_ink:
            "Insufficient Ink"
        elif pages > avalaible_paper:
            "Insufficient Paper"
        else:
            return True
        

    def printing(self):
        pages = self.pages
        while pages:
            timeformat = '{}'.format(pages)
            print("\tPrinting... ", timeformat, end='\r')
            time.sleep(0.15)
            pages -= 1
            
        

    def increaseProfit(self, price: int) -> int:
        self.profit += price
    
    def generateReport(self) -> str:
        report = f"Paper: {self.paper} \nInk: {self.ink} \nProfit: {self.profit}"
        return report
    
    def exitMsg(self):
        return "Here is your report. Thank you for using our services"

class InsufficientResourcesException(Exception):
    pass