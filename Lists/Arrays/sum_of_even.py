# Input: list of numbers from user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Initialize variables
sum_even = 0
product_odd = 1

# Loop through each number in the list
for num in numbers:
    if num % 2 == 0:
        sum_even += num
    else:
        product_odd *= num

# Display results
print("Sum of even numbers:", sum_even)
print("Product of odd numbers:", product_odd)
