from data.data import resources, FORMAT, coins

class Printer():
    def checkMode(self, mode):
        if mode == 'coloured':
            print_format = FORMAT['coloured']
        elif mode == 'greyscaled':
            print_format = FORMAT['greyscaled']
        return print_format

    def checkResource(self, mode, paper, ink, pages):
        pass

    def processPrice(pages, coin):
        price = coin * pages
        return f"Your price is {price}"

    def checkTransaction(self, coins, cost):
        if cost > coins:
            return "Insufficient funds"
        elif cost == coins:
            pass
        else:
            balance = coins - cost
            return f"Your balance is {balance}"