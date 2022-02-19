# The entry point of your application
from modules.printer import Printer

class Operation():
    on = False

    def start():
        on = True
        while on:
            response = Printer.start()
            if response is True:
                print(Printer.generateReport())
                Printer.printDocument()
                print(Printer.generateReport())
            else:
                Printer.rejectDocument()
            
    def checkResource():
        Printer.checkResource()

    def stop(self):
        self.on = False

    
    


        
if __name__== "__main__" :
    Operation.start()
