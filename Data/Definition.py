#Write a program that allows the user to:
#1) Add new definitions
#2) Search for existing definitions
#3) Delete definitions selected by him
#4) Finish

definicje = {}

while(True):
    print("1: Add Definition")
    print('2: Find Definition')
    print('3: Delete Definition')
    print("4: Finish")

   choice = input("What do you want to do?")

    if (choice == "1"):
        key = input("Enter the key (word) to define: ")
        definition = input("Enter definition: ")
        definition[key] = definition
        print("Definition added successfully")
    elif (choice == "2"):
        key = input("What are you looking for? ")
        if key in definitions:
            print(definitions[key])
        else:
            print("Definition with name not found", key)
    elif (choice == "3"):
        key = input("Which definition do you want to delete? ")
        if key in definitions:
            del definitions[key]
            print("Deleted definition named:", key)
        else:
            print("No definition named was found", key)
    elif (choice == "4"):
        print("Bye bye!")
        break
    else:
        print("You specified something out of range")

