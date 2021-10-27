class Strategy:
    def __init__(self, ll):
        self.ll = ll


class GenerateWithIterator(Strategy):
    def __call__(self, *args, **kwargs):
        self.ll.generate_random_array(use_iterator=True)


class ReadFromFile(Strategy):
    def __call__(self, *args, **kwargs):
        file_name = input('Enter file name: ')
        with open(file_name, 'r') as f:
            line = f.readline()

        nums = [float(i) for i in line.split()]

        self.ll.array_to_LL(nums)