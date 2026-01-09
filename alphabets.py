character = input("Enter a character: ")

if (character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z'):
    print(character, "is an alphabet.")
else:
    print(character, "is not an alphabet.")