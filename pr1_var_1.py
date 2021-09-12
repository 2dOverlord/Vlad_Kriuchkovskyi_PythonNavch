def main_func():
    n = int(input("Enter the N value: "))

    if n > 1000 or n < 1:
        raise ValueError

    first_bin = '0b' + ('0' * n)
    count = 0

    while len(first_bin) <= (n + 2):
        if first_bin.find('11') == -1:
            count += 1
        number = int(first_bin, 2) + 1
        first_bin = bin(number)

    print(f"The answer is {count}")

if __name__ == "__main__":
    while True:
        try:
            main_func()
            break
        except ValueError:
            print("Something gone wrong with input values, lets try again")
        except ZeroDivisionError:
            print("Something gone wrong with input values, lets try again")
