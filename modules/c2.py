
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
        
        try:
            self.ink_consumable = FORMAT[self.mode]['materials']['ink']
        except KeyError as err:
            print("No mode selected", err)

    def requestUserInput(self):
        response = input("What format would you like? greyscale or coloured: ")
        return response
    
    def processResponse(self, response):
        print("processing... ")
        self.mode = response
        self.pages = int(input("How many pages would like to print: "))
        isResourceAvailable = self.checkAvailableResources(self.mode, self.pages)
        if isResourceAvailable:
            self.displayCost()
            response = input("Proceed? y/n  ")
            if response == 'y':
                coin = input("Please Insert coin... (Penny, Nickel, Dime, or Quarter): ")
                self.coin = coin.lower()
                self.number = int(input("Enter Number of coins: "))
            else:
                self.requestUserInput()
    



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
        ink_needed = self.ink_consumable * pages

        if pages > avalaible_paper:
            print ("Insufficient Paper")
        elif ink_needed > available_ink:
            print ("Insufficient Ink")
        else:
            return True

    def displayCost(self):
        """
            - displays the printing cost
        """
        price = self.price = FORMAT[self.mode]['price']
        cost =  price * self.pages
        print(f" \n\t    MODE: {self.mode}  \n\t    PAGES: {self.pages} \n\t    COST: ${cost}")
    

class Cost(Printer):
    def __init__(self):
        Printer().__init__(self)
        

class child2(Printer):
    def __init__(self):
        Printer().__init__(self)    

class child3(Printer):
    def __init__(self):
        Printer().__init__(self) 

class child4(Printer):
    def __init__(self):
        Printer().__init__(self) 






class Printer1():
    # # class attributes
    # coin = ''
    # pages = 0
    # mode = ''
    # number = 0
    # amount = 0
    # ink_consumable = 0
    # cost = 0

    # def __init__(self, paper, ink, profit):
    #     # instance attributes
    #     self.paper = paper
    #     self.ink = ink
    #     self.profit = profit

    def requestUserInput(self):
        response = input("What format would you like? greyscale or coloured: ")
        return response

#     def startPrinter(self, response):
#         try:
#             response = input("What format would you like? greyscale or coloured: ")
#             self.mode = response
#             self.pages = int(input("How many pages would like to print: "))
#             Printer.displayCost(Printer)
#             isResource = Printer.checkAvailableResources(self, self.mode, self.pages)
#             if isResource:
#                 response = input("Proceed? y/n  ")
#                 if response == 'y':
#                     coin = input("Please Insert coin... (Penny, Nickel, Dime, or Quarter): ")
#                     self.coin = coin.lower()
#                     self.number = int(input("Enter Number of coins: "))
#                     pass
#                 else:
#                     self.start(Printer)
#             else:
#                 "Insufficient Ink or Paper"
#         except ValueError:
#             print('Incorrect Value')

#     def printDocument(self):
#         print("-----------------")
#         print("REPORT -- BEFORE")
#         report = self.generateReport(Printer, resources['ink'], resources['paper'], resources['profit'])
#         print(report)
#         ink, paper = self.processDocument(Printer)
#         print("-----------------")
#         self.printing(Printer)
#         print("-----------------")
#         print("REPORT -- AFTER")
#         report = self.generateReport(Printer, ink, paper, self.profit)
#         print(report)
#         print(self.balance(Printer, self.amount, self.cost))
       
#     def processDocument(self):
#         ink = resources['ink'] - self.ink_consumable 
#         paper = resources['paper'] - self.pages
#         self.profit += self.cost
#         return ink, paper


#     def checkAvailableResources(self, mode, pages):
#         """
#             - Check if there is sufficient amount of ink and paper
#             - if not raise error
#         """
#         available_ink = self.ink
#         avalaible_paper = self.paper
#         self.ink_consumable = FORMAT[mode]['materials']['ink'] * pages

#         if pages > avalaible_paper:
#             print("Insufficient Paper")
#         elif self.ink_consumable > available_ink:
#             ("Insufficient Ink")
#         else:
#             return True
        
#     def printing(self):
#         pages = self.pages
#         while pages:
#             timeformat = '{:2d}'.format(pages)
#             print("\tPrinting... ", timeformat, end='\r')
#             time.sleep(0.2)
#             pages -= 1
            
#     def generateReport(self, paper, ink, profit) -> str:
#         report = f"Paper: {paper} Pc \nInk: {ink} ml \nProfit: ${profit}"
#         return report

#     def report(self):
#         self.generateReport(self.paper, self.ink, self.profit)

#     def exitMsg(self):
#         return "Here is your report. Thank you for using our services"

#     def exit(self):
#         print("Exiting... ")
#         time.sleep(1)
#         return "Printing Aborted"
    
    # def off(self):
    #     print("TURNING OFF...")
    #     time.sleep(1)
    #     print("BYE..")

# class Cost(Printer):
#     def __init__(self):
#         pass

#     def displayCost(self):
#         """
#             - displays the printing cost
#         """
#         cost = FORMAT[self.mode]['price'] * self.pages
#         print(f" \n\t    MODE: {self.mode}  \n\t    PAGES: {self.pages} \n\t    COST: ${cost}")

 
#     def add_fund(self, status):
#         while status == False:
#             self.coin = input(f"Please Insert More coins... (Penny, Nickel, Dime, or Quarter) - remaining ${self.cost - self.amount}: ")
#             self.number = int(input("Enter Number of coins: "))
#             self.amount += coins[self.coin] * self.number
#             status = Printer.checkTransaction(Printer, self.cost, self.amount)
#         else:
#             self.printDocument(Printer)
        

#     def check_balance(self, amountEntered, cost):
#         balance = amountEntered - cost
#         if balance:
#             return f"Here is ${balance} in change"
    
#     def estimate_profit(self, price: int) -> int:
#         self.profit += price
        
    
#     def processPrice(self) -> int:
#         print("Processing price")
#         cost = FORMAT[self.mode]['price'] * self.pages
#         amountEntered = coins[self.coin] * self.number
#         self.cost = cost
#         self.amount = amountEntered
#         return cost, amountEntered

#     def checkTransaction(self, cost, amountEntered):
#         if cost > amountEntered:
#             return False
#         else:
#             return True

#     def transactionStatus(self, status):
#         """
#         if status is false, then cost is greater the amount entered
#         """
#         if status:
#             self.printDocument(Printer)
#         else:
#             return input("Insufficient Fund. Would like to add more fund? y/n   ")


class Print(Printer):
    pass
               



# class InsufficientResourcesException(Exception):
#     pass
