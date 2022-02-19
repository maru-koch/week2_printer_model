# The entry point of your application
from modules.printer import Printer

class Main():

    def start():
        on = True
        while on:
            Printer.start(Printer)
            cost, amount = Printer.processPrice(Printer)

            status = Printer.checkTransaction(Printer, cost, amount)
            response = Printer.transactionStatus(Printer, status)

            if response == 'y':
                Printer.addFund(Printer, status)
            else:
                msg = Printer.exit(Printer)
                print(msg)
                break
            
    def stop(self):
        self.on = False
     


if __name__== "__main__" :
    Main.start()
