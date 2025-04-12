def main():
    print("\nLet's play a tiny Mad Lib!\n")

    name = input("Enter a name: ")
    animal = input("Enter a pet's name or a friend's: ")
    place = input("Enter a place: ")
    verb = input("Enter a verb ending with -ing: ")

    # eeek that's a silly story:
    story = f"\nOne day, {name} was walking with {animal} through {place}, while {verb} and singing out loud."

    print("\nHere's the construction:\n")
    print(story)

if __name__ == "__main__":
    main()
