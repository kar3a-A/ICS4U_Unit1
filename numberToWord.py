
# Create an Algorithm to translate numbers into word.

def number_to_words(num):
    # Define lists for words
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # Break the number into parts
    units_digit = num % 10
    tens_digit = (num // 10) % 10
    hundreds_digit = num // 100

    # Initialize an empty string to store the words
    words = ""

    # Translate hundreds digit
    if hundreds_digit > 0:
        words += units[hundreds_digit] + " hundred"

    # Translate tens and units digits
    if tens_digit > 1:
        words += " " + tens[tens_digit]
        if units_digit > 0:
            words += " " + units[units_digit]
    elif tens_digit == 1:
        words += " " + teens[units_digit]
    elif units_digit > 0:
        words += " " + units[units_digit]

    return words.strip()

# Example usage:
number = int(input("Enter a number (0-999): "))
result = number_to_words(number)
print(f"The number {number} in words: {result}")

'''
This algorithm uses lists to store the words for units, teens, and tens. It then breaks the input number into its digits and translates each digit into words. The resulting words are concatenated to form the final translation.

If you run the program and input 778 you can see the output like:

Enter a number (0-999): 778
The number 778 in words: seven hundred seventy eight

'''