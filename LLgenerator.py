import random


def generate_data(nums, a, b):
    while nums > 0:
        nums -= 1
        yield float(str(random.uniform(a, b))[:6])