import random


class Node:
    def __init__(self, num):
        self.num = num
        self.next = None

    def __next__(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.headel = None

    def __str__(self):
        el = self.headel
        elms = []
        while el.next:
            elms.append(str(el.num))
            el = el.next
        elms.append(str(el.num))
        return ' '.join(elms)


    def array_to_LL(self, array):
        self.headel = Node(array[0])
        val = self.headel
        for nd in array[1:]:
            val.next = Node(nd)
            val = val.next

    def enter_from_console(self):
        n = int(input('Enter the size of an array: '))
        array = []
        for i in range(n):
            array.append(float(input(f'Enter the element {i} of array: ')))
        self.array_to_LL(array)

    def generate_random_array(self):
        n = int(input('Enter the size of an array: '))
        a = int(input('Enter the first num of range: '))
        b = int(input('Enter the second num of range: '))

        if a > b or a < 0 or b < 1:
            print('Smth gone wrong with the input: ')
            raise ValueError
        array = []
        for i in range(n):
            array.append(float(str(random.uniform(1, 10))[:6]))
        self.array_to_LL(array)

    def add_ell(self):
        val = self.headel
        k = int(input('Enter position of element: '))
        num = float(input('Enter value of element: '))
        if k == 1:
            new_val = Node(num)
            new_val.next = val
            self.headel = new_val
        else:
            for i in range(k-1):
                val = val.next
            new_val = Node(num)
            new_val.next = val.next
            val.next = new_val

    def remove_val(self):
        k = int(input('Enter position of element: '))
        val = self.headel
        if k == 1:
            self.headel = self.headel.next
        else:
            for i in range(k-1):
                val = val.next
            old_val = val.next
            new_val = old_val.next
            val.next = new_val.next
            del old_val

    def count_len(self):
        value = self.headel
        count = 1
        while value.next:
            value = value.next
            count += 1

        return count

    def __len__(self):
        return self.count_len()

    def task(self):
        index = 0
        mean = None
        value_ind = self.headel
        k = int(input('Enter the k number: '))
        if k >= len(self):
            raise ValueError('HERE')
        for i in range(len(self)-k):
            elms = [value_ind]
            time_val = value_ind
            for j in range(k):
                elms.append(time_val.next)
                time_val = time_val.next
            elms_nums = [elm.num for elm in elms]
            time_mean = sum(elms_nums) / len(elms_nums)
            if mean is None:
                mean = time_mean
            elif time_mean > mean:
                mean = time_mean

            value_ind = value_ind.next
            index += 1
        print(f'Mean value is {mean}')
        print(f'Index value is {index}')
        return mean, index