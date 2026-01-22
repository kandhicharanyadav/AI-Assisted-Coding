# Task-1 : Fibonacci Series Generator
"""def fibonacci(n):
    # Generate Fibonacci series up to n terms
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

# Get input from user
num_terms = int(input("Enter number of terms: "))
fibonacci(num_terms)"""

# Task-2 : List Reversal Function
"""def reverse_list(lst):
    # Reverse a list and return it
    return lst[::-1]

# Get input from user
user_list = input("Enter list elements (space-separated): ").split()
reversed_lst = reverse_list(user_list)
print("Reversed list:", reversed_lst)"""

"""# Task-3 : String Pattern Matching
def check_pattern(text):
    # Check if string starts with capital letter and ends with period
    return text[0].isupper() and text[-1] == '.'

# Example 1: "Hello." -> True (starts with 'H', ends with '.')
# Example 2: "hello." -> False (starts with 'h', not capital)
# Example 3: "Hello" -> False (ends with 'o', not period)

user_text = input("Enter a string: ")
if check_pattern(user_text):
    print("True")
else:
    print("False")"""

# Task-4 : Zero-shot vs Few-shot – Email Validator
"""import re
def validate_email(email):
    # Simple email validation using regex
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Get input from user
user_email = input("Enter an email: ")
if validate_email(user_email):
    print("Valid email")
else:
    print("Invalid email")"""

# Task-5 : Summing Digits of a Number
def sum_digits(num):
    # Sum all digits in a number
    return sum(int(digit) for digit in str(abs(num)))

# Get input from user
user_num = int(input("Enter a number: "))
result = sum_digits(user_num)
print("Sum of digits:", result)