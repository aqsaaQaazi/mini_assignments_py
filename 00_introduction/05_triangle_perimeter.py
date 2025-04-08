def main():
   first = float(input("Length of first side?"));
   second = float(input("Length of second side?"));
   third = float(input("Length of third side?"));
   
   perimeter = str(first + second + third);
   
   
   print(f"The perimeter of Your triangle is {perimeter}.")


# component
if __name__ == '__main__':
   main()