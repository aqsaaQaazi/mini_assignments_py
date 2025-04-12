# constants Syntax == CAPITAL_LETTERS;


def main():
    SECONDS_PER_MINUTE = 60;
    MINUTES_PER_HOUR = 60;
    HOURS_IN_A_DAY = 24;
    DAYS_IN_A_YEAR = 365;

    calculations = DAYS_IN_A_YEAR * HOURS_IN_A_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE

    print(f"There are {calculations} seconds in  a year.")
    
if __name__ == "__main__":
    main();
    
# or if we ask user for input:

def main_02():
    
    year = int(input("\nEnter a year to calculate the total seconds:"))
    
    DAYS_IN_A_YEAR = 365;
    
    seconds_in_a_year = 60* 60* 24* DAYS_IN_A_YEAR* year

    print(f"\nThere are {seconds_in_a_year} seconds in {year} years.")
    print("Leap years excluded. Using 365 days only.")
    

main_02();
