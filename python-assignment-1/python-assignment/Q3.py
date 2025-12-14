def process_numbers(numbers):

    # Remove duplicates
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)

    # Sort
    unique.sort()
    n = len(unique)

    # Mean
    total = 0
    for num in unique:
        total += num
    mean = total / n

    # Median
    if n % 2 == 1:
        median = unique[n // 2]
    else:
        median = (unique[n // 2 - 1] + unique[n // 2]) / 2

    # Mode
    mode = None
    max_count = 0
    for num in unique:
        count = 0
        for x in numbers:
            if x == num:
                count += 1
        if count > max_count:
            max_count = count
            mode = num

    print("Unique Sorted List:", unique)
    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)

try:
    data = input("Enter numbers separated by space: ").split()
    numbers = []

    for x in data:
        numbers.append(int(x))

    process_numbers(numbers)

except ValueError:
    print("Error: Please enter only integer values.")