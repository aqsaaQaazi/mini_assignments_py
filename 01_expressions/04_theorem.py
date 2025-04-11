import math

def main():
    
    
    ab = float(input("length of AB is: "))
    ac = float(input("length of AC is: "))
    
    bc = math.sqrt(
        ab ** 2 + ac ** 2
    )
    
    print(f"According to my calculations, length of BC is: {bc:.2f}")
    
    
# this condition makes the def reusable in other modules.

if __name__ == "__main__":
    main()