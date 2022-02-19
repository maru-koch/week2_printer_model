# The entry point of your application
from modules.printer import Printer

class Main():
    on = False
    
    def start():
        on = True
        while on:
            Printer.start(Printer)
            cost, amount = Printer.processPrice(Printer)
            Printer.checkTransaction(Printer, cost, amount)
            on = False
            
    def stop(self):
        self.on = False
     


if __name__== "__main__" :
    Main.start()
