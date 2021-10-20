from logic import TaskClass, MergeSort


def main():
    print('Starting programm...')
    while True:
        taskclass = TaskClass()
        commands = {'Enter array from console': taskclass.enter_from_console,
                    'Generate random array': taskclass.generate_random_array,
                    'exit': exit}
        print('Enter one of this commands: ')
        print('\n'.join(command for command in commands))
        command = input('Enter the command: ')
        try:
            commands[command]()
            print('Sorting.....')
            sort = MergeSort(taskclass)
            print(f'Sorted array is: {sort.sorted()}')
            print(f'Number of iterations is {sort.iterations}')
        except (TypeError, ValueError, KeyError):
            print('Wrong input... ')
            continue


if __name__ == '__main__':
    main()