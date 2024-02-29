def digit_sum(n):
    return sum(map(int, str(n)))

def single_digit_sum(num):
    while num >= 10:
        num = digit_sum(num)
    return num
N = int(input("Enter N value: "))
number = int(input(f"Enter {N} digit number: "))

sum_of_digits = digit_sum(number)
result = single_digit_sum(sum_of_digits)

print(f"Sum of 3 digit number: {result}")
