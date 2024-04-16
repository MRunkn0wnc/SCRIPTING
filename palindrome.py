def is_palindrome(num):
    # Convert the number to a string and check if it's equal to its reverse
    return str(num) == str(num)[::-1]

# Test the function
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")
