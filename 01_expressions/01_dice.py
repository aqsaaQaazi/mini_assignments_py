import random

dice_numbers = 6;

def roll_dice () :
    
    dice_1 = random.randint(1, dice_numbers);
    dice_2 = random.randint(1, dice_numbers);
    total = dice_1 + dice_2;
    
    print(f"total = {total}")
    
def main():
    
    # since he first twoo variables in roll dice are scope limited, theyll be unbothered by these two same names.
    
    dice_1 = 10
    dice_2 = 20 
    
    print(f"{dice_1} in main is unbothered at the start, as well as {dice_2}")
    roll_dice();
    roll_dice();
    roll_dice();
    print(f"see, {dice_1} in main is still unbothered at the end of the program, as well as {dice_2}")
    
    
if __name__ == '__main__':
    main()