
from data.data import FORMAT, resources, coins
import time

class Printer(object):
    coin = ''
    pages = 0
    mode = ''
    number = 0
    amount = 0
    ink_consumable = 0
    cost = 0
    ink = resources['ink']
    paper = resources['paper']
    profit = resources['profit']


    def start(self):
        try:
            self.mode = input("What format would you like? greyscale or coloured: ")
            self.pages = int(input("How many pages would like to print: "))
            Printer.displayCost(Printer)
            isResource = Printer.checkAvailableResources(self, self.mode, self.pages)
            if isResource:
                response = input("Proceed? y/n  ")
                if response == 'y':
                    self.coin = input("Please Insert coin... (Penny, Nickel, Dime, or Quarter): ")
                    self.number = int(input("Enter Number of coins: "))
                    pass
                else:
                    self.start(Printer)
            else:
                "Insufficient Ink or Paper"

        except ValueError:
            print('Incorrect Value')


    def printDocument(self):
        print("REPORT -- BEFORE")
        report = self.generateReport(Printer)
        print(report)
        self.processDocument(Printer)
        self.printing(Printer)
        print("REPORT -- AFTER")
        report = self.generateReport(Printer)
        print(report)
       
    def displayCost(self):
        cost = FORMAT[self.mode]['price'] * self.pages
        print(f" \n\t    MODE: {self.mode}  \n\t    PAGES: {self.pages} \n\t    COST: ${cost}")
        
    def processDocument(self):
        resources['ink'] - self.ink_consumable 
        resources['paper'] - self.pages
        self.profit += self.cost

    def processPrice(self) -> int:
        print("Processing price")
        cost = FORMAT[self.mode]['price'] * self.pages
        amountEntered = coins[self.coin] * self.number
        self.cost = cost
        self.amount = amountEntered
        return cost, amountEntered

    def checkTransaction(self, cost, amountEntered):
        if cost > amountEntered:
            return False
        else:
            return True

    def transactionStatus(self, status):
        """
        if status is false, then cost is greater the amount entered
        """
        if status:
            self.printDocument(Printer)
        else:
            return input("Insufficient Fund. Would like to add more fund? y/n   ")
    
    def addFund(self, status):
        while status == False:
            self.coin = input(f"Please Insert More coins... (Penny, Nickel, Dime, or Quarter) - remaining ${self.cost - self.amount}: ")
            self.number = int(input("Enter Number of coins: "))
            self.amount += coins[self.coin] * self.number
            status = Printer.checkTransaction(Printer, self.cost, self.amount)
        else:
            self.printDocument(Printer)
        

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
        self.ink_consumable = FORMAT[mode]['materials']['ink'] * pages

        if self.ink_consumable > available_ink:
            print("Insufficient Ink")
        elif pages > avalaible_paper:
            ("Insufficient Paper")
        else:
            return True
        
    def printing(self):
        time.sleep(1)
        pages = self.pages
        while pages:
            timeformat = '{}'.format(pages)
            print("\tPrinting... ", timeformat, end='\r')
            time.sleep(0.2)
            pages -= 1
            
    def increaseProfit(self, price: int) -> int:
        self.profit += price
    
    def generateReport(self) -> str:
        report = f"Paper: {self.paper} \nInk: {self.ink} \nProfit: {self.profit}"
        return report
    
    def exitMsg(self):
        return "Here is your report. Thank you for using our services"

    def exit(self):
        print("Exiting... ")
        time.sleep(1)
        return "Printing Aborted"

class InsufficientResourcesException(Exception):
    pass
