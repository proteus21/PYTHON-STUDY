#-----------------------------------
# Create definition via dictionary
# Small programme 2
#----------------------------------

definitions = {}
while (True):
    print(" : Add definitions, 2: Find definitions, 3: Delete definitions, 4: Finish")
    choice= input( "what do you want to do?")

    if (choice =="1") :
        key = input("Enter key to deinnify:")
        definition =input(" Give definition :")
        definitions[key] = definition
        print( " Definition successfully entered")

    elif (choice =="2"):
        key = input("Enter a word to search for:")
        if key in definitions:
           print(definitions[key])
        else:
           print("Not found")
    elif (choice =="3"):
        key = input("Enter word to delete:")
        if key in definitions:
            del definitions[key]
            print("Key removed")
        else:
            print("Key not found")
    elif (choice == "4"):
        print("Bye bye")
        break
    else:
            print("You have specified something out of range")
