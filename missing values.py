def find_missing_numbers(series):
    missing_numbers = []
    for i in range(len(series) - 1):
        if series[i + 1] - series[i] > 1:
            missing_numbers.append(series[i] + 1)
            missing_numbers.append(series[i + 1] - 1)
    return missing_numbers

def main():
    # Given series
    series = [1, 5, 11, 19]

    # Find the missing numbers in the series
    missing_numbers = find_missing_numbers(series)

    # Print the missing numbers
    print("The missing numbers in the series are:", missing_numbers)


