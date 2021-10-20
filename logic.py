import random


class TaskClass:
    def __init__(self):
        self.array = []

    def enter_from_console(self):
        n = int(input('Enter the size of an array: '))
        for i in range(n):
            self.array.append(float(input(f'Enter the element {i} of array: ')))

    def generate_random_array(self):
        n = int(input('Enter the size of an array: '))
        a = int(input('Enter the first num of range: '))
        b = int(input('Enter the second num of range: '))

        if a > b or a < 0 or b < 1:
            print('Smth gone wrong with the input: ')
            raise ValueError

        for i in range(n):
            self.array.append(float(str(random.uniform(1, 10))[:6]))

        print(f'The array is: {self.array}')



class MergeSort:
    def __init__(self, taskclass):
        self.array = taskclass.array
        self.iterations = 0

    def merge_sides(self, left, right):
        output = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            self.iterations += 1
            if left[i] < right[j]:
                output.append(left[i])
                i += 1
            else:
                output.append(right[j])
                j += 1

        for a in left[i:]:
            output.append(a)
        for a in right[j:]:
            output.append(a)

        return output

    def sort(self, list):
        list_length = len(list)

        if list_length <= 1:
            return list

        mid = list_length // 2

        left_partition = self.sort(list[:mid])
        right_partition = self.sort(list[mid:])

        return self.merge_sides(left_partition, right_partition)

    def sorted(self):
        return self.sort(self.array[:])