import random 

def main():
    
    roll_1 = random.randint(1,6);
    roll_2 = random.randint(1,6);
    
    sum_rolls = roll_1 + roll_2
    
    print("\n__DICE ROLLS__\n")
    print(f"You got {roll_1} & {roll_2}, if we add these up we get {sum_rolls}")


if __name__ == "__main__":
    main();   