import random


class Iterator:
    def __init__(self, num_of_el, a, b):
        self.num_of_el = num_of_el
        self.a = a
        self.b = b

    def __next__(self):
        while self.num_of_el > 0:
            self.num_of_el -= 1
            return float(str(random.uniform(self.a, self.b))[:6])
        raise StopIteration

    def __iter__(self):
        return self
