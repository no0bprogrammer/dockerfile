def print_diamond(n):
    # Print the upper part of the diamond
    for i in range(n):
        # Print leading spaces
        print(" " * (n - i - 1), end="")
        # Print the stars
        print("*" * (2 * i + 1))

    # Print the lower part of the diamond
    for i in range(n - 2, -1, -1):
        # Print leading spaces
        print(" " * (n - i - 1), end="")
        # Print the stars
        print("*" * (2 * i + 1))

# Call the function to print the diamond pattern
n = 50  # You can change this value to make the diamond bigger or smaller
print_diamond(n)

