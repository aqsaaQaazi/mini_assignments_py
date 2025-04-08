# ask user for their favorite animal and respond with interest in the same:


def main ():
    print("\n Hey, i was curious to know about your favorite animal.. it can be anything A Pet, A Domestic Animal, or Wild. ")
    animal = input("\n what's that? ")
    
    
    # i'm using ansi escape codes for bold & italics, dk if its a good approach or not. 
    prompt_reply = print(f"\n Great minds think alike, \033[1m\033[3m{animal}s\033[0m are my favorite too!")
    

# modular 
if __name__ == '__main__':
    main()