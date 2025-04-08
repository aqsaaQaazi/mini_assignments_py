# a program that converts fahrenheit into celsius and vice versa. 


    # Temperature Converter: Celsius <-> Fahrenheit
    


def main():
        """
        The main function converts temperatures between Celsius and Fahrenheit based on user input.
        """
    
        def to_fahrenheit(c):
                return (c * 9/5) + 32

        def to_celsius(f):
                return (f - 32) * 5/9
        print("\n Temperature Converter\n ")

        print("\nChoose an option:\n")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius\n")

        choice = input("Enter 1 or 2: ")

        if choice == "1":
            
            c = float(input("Enter temperature in Celsius: "))
            f = to_fahrenheit(c)
            
            # .2f rounds float to 2 decimals
            print(f"{c}°C is equal to {f:.1f}°F")
            
        elif choice == "2":
            
            f = float(input("Enter temperature in Fahrenheit: "))
            c = to_celsius(f)
            
            print(f"{f}°F is equal to {c:.1f}°C")
        else:
            print("\nchoose from the options above. (1-2)")



# modular
if __name__ == '__main__':
    main()
    
    # asked AI for formula: here's the answer:
    
"""what is the formula for conerting basic tempratures? f ino c and vice versa


ChatGPT said:
Here are the basic temperature conversion formulas between Fahrenheit (°F) and Celsius (°C):

🔁 Celsius to Fahrenheit:
°
𝐹
=
(
°
𝐶
×
9
5
)
+
32
°F=(°C× 
5
9
​
 )+32
✅ Multiply Celsius by 9/5, then add 32.

🔁 Fahrenheit to Celsius:
°
𝐶
=
(
°
𝐹
−
32
)
×
5
9
°C=(°F−32)× 
9
5
​
 
✅ Subtract 32 from Fahrenheit, then multiply by 5/9.

🧪 Examples:
25°C to °F:

(
25
×
9
/
5
)
+
32
=
45
+
32
=
77
°
𝐹
(25×9/5)+32=45+32=77°F
77°F to °C:

(
77
−
32
)
×
5
/
9
=
45
×
5
/
9
=
25
°
𝐶
(77−32)×5/9=45×5/9=25°C
Let me know if you want formulas for Kelvin too!
    """