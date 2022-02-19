# The entry point of your application
from modules.printer import Printer

class Main():
    on = False
    
    def start():
        on = True
        while on:
            if Printer.start(Printer):
                Printer.generateReport(Printer)
                Printer.printDocument(Printer)
                Printer.generateReport(Printer)
            
    def stop(self):
        self.on = False
     


if __name__== "__main__" :
    Main.start()
