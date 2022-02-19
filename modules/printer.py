
from data.data import FORMAT, resources, coins

class Printer():
    coin = ''
    pages = 0
    mode = ''
    number = 0

    def __init__(self):
        self.ink = resources['ink']
        self.paper = resources['paper']

    def start(self):
        self.mode = input("What format would you like? greyscale or coloured: ")
        self.pages = int(input("How many pages would like to print: "))
        self.coin = input("Please Insert coin... (Penny, Nickel, Dime, or Quarter): ").islower()
        self.number = int(input("Enter Number of coins: "))
        response = Printer.checkAvailableResources(self.mode, self.pages)
        return response

    def checkMode(self, mode):
        if mode == 'coloured':
            print_format = FORMAT['coloured']
        elif mode == 'greyscaled':
            print_format = FORMAT['greyscaled']
        return print_format

    def printDocument():
        resources['ink'] - ink 
        resources['paper'] - paper 
        Printer.increaseProfit()
    
    def rejectDocument():
        print("Document rejected")

    def checkResource(self, mode, paper, ink, pages):
        pass

    def processPrice(pages, mode, coin, number) -> int:
        cost = FORMAT[mode]['price'] * pages
        amountEntered = coins[coin] * number
        return cost, amountEntered

    def checkTransaction():
        cost, amountEntered = Printer.processPrice()
        if cost > amountEntered:
            return "Insufficient funds"
        elif amountEntered == cost:
            return True
        else:
            Printer.balance(amountEntered, cost)
            return True

    def balance(amountEntered, cost):
        balance = amountEntered - cost
        return f"Here is ${balance} in change"

    def checkAvailableResources(mode, pages):
        """
            - Check if there is sufficient amount of ink and paper
            - if not raise error
        """
        available_ink = resources['ink']
        avalaible_paper = resources['paper']
        ink = FORMAT[mode]['materials']['ink'] * pages
        if ink > available_ink or pages > avalaible_paper:
            raise InsufficientResourcesException
        else:
            return True

    def increaseProfit(self, price: int) -> int:
        resources['profit'] += price
         
    def generateReport() -> str:
        report = f"Paper: {resources['paper']} \nInk: {resources['ink']} \nProfit: {resources['profit']}"
        return report
    
    def exitMsg(self):
        return "Here is your report. Thank you for using our services"

class InsufficientResourcesException(Exception):
    pass