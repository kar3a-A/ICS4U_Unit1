
# Get the number of terms from the user
nterms = int(input("How many terms? "))

# Initialize the first two terms
n1, n2 = 0, 1

# Check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    # If there's only one term, return n1
    print("Fibonacci sequence up to", nterms, ":")
    print(n1)
else:
    # Generate the Fibonacci sequence
    print("Fibonacci sequence:")
    count = 0
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # Update values for the next iteration
        n1 = n2
        n2 = nth
        count += 1
