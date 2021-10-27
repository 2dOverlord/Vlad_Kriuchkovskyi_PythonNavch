from logic import LinkedList
from strategy import GenerateWithIterator, ReadFromFile


class StrategyManager:
    def __init__(self, ll):
        self.ll = ll

    def __call__(self, *args, **kwargs):
        options = ('Generate randomly', 'Enter from file')
        print('Here are options of the data entering: ')
        for option in options:
            print(option)
        command = input('Now type any command you want to run: ')

        if command == options[0]:
            strategy = GenerateWithIterator(self.ll)
            strategy()
        elif command == options[1]:
            strategy = ReadFromFile(self.ll)
            strategy()
        else:
            raise ValueError


class Manager:
    def __init__(self):
        self.ll = LinkedList()
        self.strategy = StrategyManager(self.ll)
        self.options = {
            # 'Generate randomly': self.ll.generate_random_array,
            # 'Enter ll': self.ll.enter_from_console,
            'Enter data': self.strategy,
            'Add element': self.ll.add_ell,
            'Remove element': self.ll.remove_val,
            'Run task': self.ll.task,
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
                print(self.ll)
            except (KeyError, TypeError, ValueError, AttributeError, FileNotFoundError) as err:
                print('Smth has gone wrong with the input')