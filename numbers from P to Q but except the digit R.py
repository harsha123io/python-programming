def contains_digit(number, digit):
    return str(digit) in str(number)

def print_numbers_excluding_digit(p, q, r):
    for num in range(p, q + 1):
        if not contains_digit(num, r):
            print(num)
p = int(input("Enter the starting number (P): "))
q = int(input("Enter the ending number (Q): "))
r = int(input("Enter the digit to exclude (R): "))

print_numbers_excluding_digit(p, q, r)
