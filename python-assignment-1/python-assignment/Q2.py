import sys

string = input("Enter a string: ")

while True:
    print("\nMENU")
    print("1. Convert string to uppercase")
    print("2. Count occurrences of a character")
    print("3. Check if string starts with a prefix")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Uppercase string:", string.upper())

    elif choice == 2:
        ch = input("Enter character to count: ")
        print("Count:", string.count(ch))

    elif choice == 3:
        prefix = input("Enter prefix: ")
        if string.startswith(prefix):
            print("Yes, the string starts with the given prefix")
        else:
            print("No, the string does not start with the given prefix")

    elif choice == 4:
        print("Exiting program")
        sys.exit()

    else:
        print("Invalid choice. Try again.")
