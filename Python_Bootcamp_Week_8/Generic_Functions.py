from Register_Classes import ValueOutOfRange

def RunMenu(menuList):

    continueLoop = True
    while continueLoop == True:

        try: #Tells the compiler to attempt the code indented, passing to an exception if an error occurs
            
            #Start text to the screen with the initial value in the passed list
            print(menuList[0])

            for x in range(1, len(menuList)): #Loops from 1 (because be have used index 0 already), until the end of the indexes in our passed list
                print(str(x) + ": " + menuList[x]) #Prints out a formatted text screen, using the text passed up to the function inside the list, using x as the index counter

            menuChoice = int(input("\nPlease make a selection from the list provided:\n")) #Requests the user enter an int - then saves it into the variable assignment

            if menuChoice > len(menuList) - 1 or menuChoice < 1:
                raise ValueOutOfRange #Raises the custom exception if the IF statement validates as TRUE

        except ValueOutOfRange: #Triggers when the user enters a value outside of the list range provided

            print("\n\nError! PLease only enter a number from the list indicated, please try again...")
            input("[Press Enter to Try Again]\n\n")

        except ValueError: #Triggers when the user enters a non-integer value

            print("\n\nError! PLease only enter a valid whole number, please try again...")
            input("[Press Enter to Try Again]\n\n")

        except: #Triggers exception - no specific condition required.

            print("\n\nError! An unknown bug as occurred, please try again...")
            input("[Press Enter to Try Again]\n\n")

        else: #Triggers only when no exception has been raised!

            continueLoop = False
            return menuChoice #Returns the user's input

def DisplayAllStudents(myStudents): #Function to display off students currently logged in the system
    
    print("\n-----------Unassigned Students-----------\n\n")

    for x in range(0, len(myStudents)):

        print("\nName: " + myStudents[x].firstName + " " + myStudents[x].secondName)
        print("Age: " + str(myStudents[x].age))

def DisplayStudentsBySubject(myClasses, SubjectIndex):

    if len(myClasses[SubjectIndex].classStudents) == 0:

        print("\n-----------" + myClasses[SubjectIndex].className + "-----------\n\n")
        print("There are currently no Students assigned to this subject...\n")

    else:

        print("\n-----------" + myClasses[SubjectIndex].className + "-----------\n\n")

        for x in range(0, len(myClasses[SubjectIndex].classStudents)):

            print("\nName: " + myClasses[SubjectIndex].classStudents[x].GetName())
            print("Age: " + str(myClasses[SubjectIndex].classStudents[x].age))

def StudentSelectionMenu(myStudents, titleMsg, listMsg):

    print("\n" + titleMsg + "\n\n")

    menuList = [listMsg + "\n"]
    for x in range(0, len(myStudents)):
        menuList.append(myStudents[x].firstName + " " + myStudents[x].secondName)
    menuList.append("Return to Menu")

    return RunMenu(menuList)