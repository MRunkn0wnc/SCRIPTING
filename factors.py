def print_factors(n):
    print("Factors of", n, "are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

# Test the function
number = int(input("Enter a number: "))
print_factors(number)
