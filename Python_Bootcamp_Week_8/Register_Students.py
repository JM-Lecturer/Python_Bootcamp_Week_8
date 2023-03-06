def RegStudents(myStudents): #This section will be used to add new student to the myStudents List

    continueLoop = True
    while continueLoop == True:
    
        DisplayAllStudents(myStudents)

        menuList = ["\n------------Register New Student Menu------------\n\n", "Add New Student", "Exit"]
        menuChoice = RunMenu(menuList)

        inputDetails = list() #This is a temp list to store input values for validation - before the data is placed in side of our object list

        if menuChoice == 1:

            inputDetails.append(input("\n\nPlease enter the students first name:\n"))
            inputDetails.append(input("\n\nPlease enter the students seocond name:\n"))

            ageLoop = True
            while ageLoop == True: #This will loop to ensure the user enters the correct age - without forcing them to re-enter all the details

                try:

                    inputDetails.append(int(input("\n\nPlease enter the students age:\n")))

                    if inputDetails[2] < 16 or inputDetails[2] > 120:
                        raise ValueOutOfRange

                except ValueError:

                    print("\n\nPlease only enter in a whole number...")
                    input("[Press Enter to Try Again]")
                    inputDetails.pop()

                except ValueOutOfRange:

                    print("\n\nStudents must be 16 or older, and no older than 120...")
                    input("[Press Enter to Try Again]")
                    inputDetails.pop()

                except:

                    print("\n\nUnknown error has occured, please try again...")
                    input("[Press Enter to Try Again]")
                    inputDetails.pop()

                else:

                    print("\n\n-----------------------------------------------------")
                    print("\nFirst Name: " + inputDetails[0] + "\nSecond Name: " + inputDetails[1] + "\nAge: " + str(inputDetails[2]))

                    menuList = ["\nAre you happy with these details?\n", "Yes" , "No"]
                    menuChoice = RunMenu(menuList)

                    if menuChoice == 1:
                        ageLoop = False
                        print("\n\nNew Student Added!")
                        input("[Press Enter to Continue]\n\n")
                        myStudents.append(Students(inputDetails[0], inputDetails[1], inputDetails[2]))
                    elif menuChoice == 2:
                        ageLoop = False

        elif menuChoice == 2:
            continueLoop = False
