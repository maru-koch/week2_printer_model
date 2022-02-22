# The entry point of your application
from data.data import FORMAT, resources, coins
from assets.art import logo
from modules.printer import Operations

class Printer(Operations):
    options =['greyscale', 'coloured']
    def start(self):
        print(logo)
        while self.power:
            try:
                response = self.requestUserInput()
                if response == 'off':
                    self.off()
                elif response == 'report':
                    self.report()
                elif response in self.options:
                    self.processResponse(response)
                else:
                    raise ValueError
            except ValueError:
                print("Unkown Value")
            finally:
                pass
    
if __name__== "__main__" :

    ink = resources['ink']
    paper = resources['paper']
    profit = resources['profit']

    DecaPrinter = Printer(paper, ink, profit)
    DecaPrinter.start()
