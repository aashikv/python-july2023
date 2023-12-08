def print_positive_numbers(start, end):
    for num in range(start, end + 1):
        if num > 0:
            print(num)


start_range = int(input("Enter the starting number: "))
end_range = int(input("Enter the ending number: "))

print("Positive numbers in the range:")
print_positive_numbers(start_range,end_range)
