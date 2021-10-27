from logic import LinkedList
from strategy import GenerateWithIterator, ReadFromFile


class StrategyManager:
    def __init__(self, ll):
        self.ll = ll

    def set_first_strategy(self):
        self.strategy = GenerateWithIterator(self.ll)

    def set_second_strategy(self):
        self.strategy = ReadFromFile(self.ll)

    def __call__(self, *args, **kwargs):
        try:
            self.strategy()
        except AttributeError:
            print('Strategy has not been said yet')


class Manager:
    def __init__(self):
        self.ll = LinkedList()
        self.strategy = StrategyManager(self.ll)
        self.options = {
            'Generate with iterator': self.strategy.set_first_strategy,
            'Enter from text file': self.strategy.set_second_strategy,
            'Input': self.strategy,
            'Add element': self.ll.add_ell,
            'Remove element': self.ll.remove_val,
            'Run task': self.ll.task,
            'Print': self.ll.__str__,
            'exit': exit,
        }

    def __call__(self, *args, **kwargs):
        while True:
            print('Here are options of the program: ')
            for option in self.options:
                print(option)
            command = input('Now type any command you want to run: ')
            try:
                if command in ('Add element', 'Remove element', 'Run task') and self.ll.headel is None:
                    print('You cant do this till you will enter an LL')
                    continue
                self.options[command]()
            except (KeyError, TypeError, ValueError, AttributeError, FileNotFoundError) as err:
                print(err)
                print('Smth has gone wrong with the input')