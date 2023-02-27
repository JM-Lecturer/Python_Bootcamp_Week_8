def RunMenu(menuList):

    #Start text to the screen with the initial value in the passed list
    print(menuList[0])

    for x in range(1, len(menuList)): #Loops from 1 (because be have used index 0 already), until the end of the indexes in our passed list
        print(x + ": " + menuList[x]) #Prints out a formatted text screen, using the text passed up to the function inside the list, using x as the index counter

    menuChoice = int(input("\nPlease make a selection from the list provided:\n")) #Requests the user enter an int - then saves it into the variable assignment

    return menuChoice #Returns the user's input

continueLoop = True #Sets my loop condition variable to True
while continueLoop == True: #Will loop this section of code until the variable condition is changed to false

    #Assign text to a list, ready to be passed into the RunMenu function
    menuList = ["------------Menu------------\n\n", "Register Student", "Assign Student to Class", "Take Register", "Exit"]

    #Triggers the RunMenu Function, with the list passed into it
    menuChoice = RunMenu(menuList)

    #This will be the If statement used to make a selection based on what the user has input in the menu function
    if menuChoice == 1:
        print("Register Students coming soon...")
    elif menuChoice == 2:
        print("Assign students coming soon...")
    elif menuChoice == 3:
        print("Take Register coming soon...")
    else:
        print("Goodbye!")
        continueLoop = False #Reassign the loop condition variable to false to break the loop and close the program