## Normal
#? Note
#* def
#! 

#* Binary search: a searching technique that works on a sorted array or list of elements.
#* it repeatedly dividng the search interval in half, by comparing the target value with the middle number and 
#* eliminating half of the remaining elements.

#Linear Search
array=[1,4,3,5,7,2,9]
value=int(input("Insert the number value you want to find in the array")) #4
for i in range(len(array)):
    if value==array[i]:
        found= True
        break
if found==True:
    print("Found at position ",i+1,)

else:
    print("Not found")


#* Linear Search: that finds the position of a target value within a list by checking each element in sequence 
#* until a match is found or the entire list has been searched.

#Binary Search, it is more efficient to use in searching array that has many value, as it fold in half and search in only one side that the value is located in by calculation.
array=[1,4,3,5,7,2,9]
array.sort()
print(array)
value=int(input("Enter the value you want to search"))
start=0
end=len(array)-1
found=False
while start <= end and found==False:
    mid=(start+end)//2
    if value == array[mid]:
        found=True
        position=mid
    elif value > array[mid]:
        start = mid + 1
    else:
        end = mid - 1
if found:
    print("Found at position : ", position + 1)
else:
    print("Not found")

#* Algorithm: An algorithm is a step-by-step procedure or set of rules for solving a specific problem or accomplishing a particular task.

# Example: A simple algorithm for finding the maximum number in a list:
lst=[1,5,6,7,3,4]
def find_max_number(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

print('max number is ', find_max_number(lst))

#? Bubble sorting: Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

#Bubble sort
mylist=[23,1,2,3,4,5,6]
for j in range(len(mylist)-1):
    swap = False
    for i in range(len(mylist)-1):
        
        if mylist[i] > mylist[i+1]:
            temp=mylist[i]
            mylist[i]=mylist[i+1]
            mylist[i+1]=temp
            swap=True
        
print(mylist)

#? User Manual: A user manual is a document that provides instructions, information, or guidelines on how to use a product or system. It typically includes details on installation, setup, operation, and troubleshooting.
#? example The user manual for a smartphone that provides instructions on how to set up the device, use its features, and troubleshoot common issues.

# Compute the program with an algorithm to print sum and product of an array.
def calculate_sum_and_product(arr):
    # Initialize variables to store the sum and product
    sum_result = 0
    product_result = 1

    # Calculate sum and product
    for num in arr:
        sum_result += num
        product_result *= num

    return sum_result, product_result

# Example usage:
input_array = [1, 2, 3, 4, 5]
sum_result, product_result = calculate_sum_and_product(input_array)

# Display the results
print(f"Sum of the array: {sum_result}")
print(f"Product of the array: {product_result}")

''' ⬇️⬇️⬇️
In this program:
•	The function calculate_sum_and_product takes an array as input.
•	It initializes two variables (sum_result and product_result) to store the sum and product, respectively.
•	It then iterates through each element of the array, updating the sum and product accordingly.
•	Finally, the function returns the calculated sum and product.
•	An example array (input_array) is provided, and the results are printed.

Output:

Sum of the array: 15
Product of the array: 120

'''
# ---
'''
Explain what is software testing and basis of software testing? List different types of testing for software project to ensure program correctness. 

Software Testing 
Software testing is the process of evaluation a software item to detect differences between given input and expected output. Also to assess the feature of A software item. Testing assesses the quality of the product. Software testing is a process that should be done during the development process. In other words software testing is a verification and validation process. 
Basics of software testing 
There are two basics of software testing: blackbox testing and whitebox testing. 
Blackbox Testing 
Black box testing is a testing technique that ignores the internal mechanism of the system and focuses on the output generated against any input and execution of the system. It is also called functional testing. 
Whitebox Testing 
White box testing is a testing technique that takes into account the internal mechanism of a system. It is also called structural testing and glass box testing. 
Black box testing is often used for validation and white box testing is often used for verification. 
Types of testing 
There are many types of testing like 
1.	Unit Testing:                Verify individual components work as intended.
2.	Integration Testing:    Test interactions between integrated components.
3.	Functional Testing:     Evaluate software functionality against requirements.
4.	System Testing:           Assess the complete software system's compliance.
5.	Stress Testing:             Evaluate system performance under extreme conditions.
6.	Performance Testing: Assess responsiveness and speed under normal conditions.
7.	Usability Testing:        Evaluate user-friendliness and overall user experience.
8.	Acceptance Testing:    Confirm software meets user requirements.
9.	Regression Testing:     Ensure new changes don't impact existing functionality.
10.	Beta Testing:                Release software to limited users for real-world testing.

'''
# ---
'''
Device the program to print 2D array in Matrix form.

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
print_matrix(matrix)

Explanation:
1.	The print_matrix function takes a 2D array (matrix) as input.
2.	It uses nested loops to iterate through each row and element of the matrix.
3.	The print function is used to print each element, and end="\t" is used to separate elements with a tab.
4.	After printing each row, a new line is added to move to the next row.

When we run this program, it will output the matrix in a readable format:
Matrix:
1       2       3
4       5       6
7       8       9

'''