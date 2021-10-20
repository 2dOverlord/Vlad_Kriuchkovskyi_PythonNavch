from logic import LinkedList

class Manager:
    def __init__(self):
        self.ll = LinkedList()
        self.options = {
            'Generate randomly': self.ll.generate_random_array,
            'Enter ll': self.ll.enter_from_console,
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
            except (KeyError, TypeError, ValueError, AttributeError) as err:
                print('Smth has gone wrong with the input')