def getSum(numbers, negative=False):
    if negative:
        filtered_numbers = [num for num in numbers if num >= 0]
    else:
        filtered_numbers = numbers
    return sum(filtered_numbers)

user_input = input("Enter a list of numbers separated by spaces: ")
user_numbers = [int(num) for num in user_input.split()]

negative_input = input("Do you want to exclude negative numbers?   `yes or no` ").strip().lower()
if negative_input == "yes":
    negative = True
else:
    negative = False

result = getSum(user_numbers, negative)

if negative:
    print("Sum of positive numbers:", result)
else:
    print("Sum of all numbers (including negative):", result)
