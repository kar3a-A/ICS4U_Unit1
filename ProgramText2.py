## Normal
#? Note
#* def

# U1 A8 Matrix
A= [[1,2,3],
    [2,2,2]]
B =[[3,2],
    [2,3],
    [2,2]]
C= [[0,0],
    [0,0]]
Arows = len(A)
Bcols = len(B[0])
Brows = len(B)

for i in range(Arows):
    for j in range(Bcols):
        for k in range(Brows):
            C[i][j] += A[i][k] * B[k][j]
for r in C:
    print(r)

#* 1-D array: simple data structure that stores a single list of elements, all have same data type.
#* It allows random access, using its index.
#* 2-D array: consists of a list of arrays, where each has similar data types.
#* can be seen as a collection of 1D arrays or a matrix.
#* It allows random access using both row and column indices.

# Creating a 1D array (list)
my_list = [1, 2, 3, 4, 5]

# Creating a 2D array (matrix)
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in my_matrix:
    print(i)
    
# Fabonacci loop
def fibonacci_loop(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

n_terms = int(input("Enter the number of terms: "))
fib_result = fibonacci_loop(n_terms)
print(f"Fibonacci sequence up to {n_terms} terms:")
print(*fib_result)

# another way
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n_terms = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence up to {n_terms} terms:")
for i in range(n_terms):
    print(fibonacci_recursive(i), end=" ")