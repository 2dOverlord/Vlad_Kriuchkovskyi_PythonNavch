def rec_main(n):
    if n < 1:
        return 0
    if n == 1:
        return 2
    if n == 2:
        return 3
    return rec_main(n - 1) + rec_main(n - 2);


def c_input():
    return int(input("Enter the N value: "))


def check_input(n):
    if n > 1000 or n < 1:
        raise ValueError


if __name__ == '__main__':
    try:
        n = c_input()
        check_input(n)
        sol = rec_main(n)
        print(f'The solution is {sol}')
    except ValueError:
        print('Smth gone wrong with input')
