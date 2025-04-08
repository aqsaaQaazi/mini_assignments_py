"""Prompt the user to enter the first number.

Read the input and convert it to an integer.

Prompt the user to enter the second number.

Read the input and convert it to an integer.

Calculate the sum of the two numbers.

Calculate the sum of the two numbers
"""


print( "\n lets Add up: ")
    
first_input = input("\n Enter a number: ");
first_input = int(first_input);
second_input = input("\n Enter another number: ")
second_input = int(second_input)

def sum():
        total = first_input + second_input
        print(f"this program says, The sum of {first_input} & {second_input} is {total}.");
    
sum();



if __name__ == '__sum__':
    sum()