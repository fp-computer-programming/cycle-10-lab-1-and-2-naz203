"""

Create a Python file named lab_10-1.py
*** You must write a comment for every chunk of code you write from now on along with your author tag***

Using a while loop, write a program that prompts the user to input a number.
If the user inputs a number, add that to the sum of the previous numbers entered.
If the user enters -1, the program should end and display the sum of all the numbers entered.
Be sure the program uses a break statement
_____________________________________________________________________________________________________________

Create a Python file named lab_10-2.py
Using the same approach as lab 1, write a program that prints all the numbers that are multiples of 3 in a list. Be sure your program uses a continue statemen


"""

10-1


# Author: naz
# Description: A program using a while loop to prompt the user for numbers, adding them until -1 is entered.


sum_of_numbers = 0


while True:
    user_input = input("Enter a number (or -1 to end): ")
    
    # Check if the input is a valid number
    if user_input.isdigit():
        num = int(user_input)
        
        # Check if the number is -1 to break the loop
        if num == -1:
            break
        
        sum_of_numbers += num


# Display the sum of all entered numbers
print(f"Sum of numbers entered: {sum_of_numbers}")





10-2

# Author: nazeer
# Description: A program using a while loop to print multiples of 3 from user input.


while True:
    user_input = input("Enter a number (or -1 to end): ")
    
    # Check if the input is a valid number
    if user_input.isdigit():
        num = int(user_input)
        
        # Check if the number is -1 to break the loop
        if num == -1:
            break
        
        # Check if the number is a multiple of 3
        if num % 3 != 0:
            continue
        
        # Print the multiple of 3
        print(f"Multiple of 3: {num}")
