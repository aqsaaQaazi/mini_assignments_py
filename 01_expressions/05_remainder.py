def main ():
    numerator = int(input("Enter the numerator:"))
    denominator = int(input("denominator: "))
    
    if denominator == 0:
        print("Division by zero is not allowed.")
        return
    
    quotient = numerator // denominator
    remainder = numerator % denominator
    
    
    if remainder != 0:
        print(f"When we divide {numerator} by {denominator}, we get {quotient} with a remainder of {remainder}.")
    else:
        print(f"When we divide {numerator} by {denominator}, we get {quotient}.")

if __name__ == "__main__":
    main()