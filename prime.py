def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

# Take input from the user
number = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

