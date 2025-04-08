def main():
    user_input = float(input("Enter a number to calculate its square: "))
    result = str(user_input ** 2)
    
    output_message = f"Square of {user_input} is {result}."
    
    print(output_message);

if __name__ == '__main__':
    main()