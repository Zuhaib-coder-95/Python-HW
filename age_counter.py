try:
    age_input = input("Please enter your age: ")
    age = int(age_input)
    
    if age % 2 == 0:
        print("The age is even.")
    else:
        print("The age is odd.")

except ValueError:
    print("Value error: Please enter a whole number (integer) only.")