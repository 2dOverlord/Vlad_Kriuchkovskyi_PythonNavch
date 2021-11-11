class Strategy:
    def __init__(self, ll):
        self.ll = ll

    def __call__(self, *args, **kwargs):
        self.position = int(input('Enter position: '))


class GenerateWithIterator(Strategy):
    def __call__(self, *args, **kwargs):
        super().__call__()
        self.ll.generate_random_array(use_iterator=True, position=self.position)


class ReadFromFile(Strategy):
    def __call__(self, *args, **kwargs):
        super().__call__()
        file_name = input('Enter file name: ')
        with open(file_name, 'r') as f:
            line = f.readline()

        nums = [float(i) for i in line.split()]

        self.ll.array_to_LL(nums, position=self.position)