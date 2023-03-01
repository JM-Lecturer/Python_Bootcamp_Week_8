class ValueOutOfRange(Exception):
    #This class is for triggering a custom exception
    pass

class Students(): #Class template for student objects

    #These are the member attributes/variables to define our object
    firstName = ""
    secondName = ""
    age = 0
    className = ""
    Attendance = False

    def __init__(self, firstName, secondName, age): #Constructor used to initialize our student objects

        self.firstName = firstName
        self.secondName = secondName
        self.age = age

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
    
    for x in range(0, len(myStudents)):

        print("\nName: " + myStudents[x].firstName + " " + myStudents[x].secondName)
        print("Age: " + str(myStudents[x].age))
        
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

def AssignStudents(myStudents, myClasses):

    continueLoop = True
    while continueLoop == True:
    
        DisplayAllStudents(myStudents)

        print("\n------------Assign Students------------\n\n")

        menuList = ["Which student would you like to assign to a class?\n"]
        for x in range(0, len(myStudents)):
            menuList.append(myStudents[x].firstName + " " + myStudents[x].secondName)
        menuList.append("Return to Menu")

        studentChoice = RunMenu(menuList)

        if studentChoice == len(menuList) - 1:
            continueLoop = False
        else:

            classLoop = True
            while classLoop == True:

                menuList = ["\n\nWhich class wouild you like to assign " + myStudents[studentChoice - 1].firstName + " " + myStudents[studentChoice - 1].secondName + " to:\n"]
                for x in range(0, len(myClasses)):
                    menuList.append(myClasses[x])
                menuList.append("Return")

                classChoice = RunMenu(menuList)

            #myStudents[menuChoice - 1].className = "sdasf"


#-----------------------------Main Code Here------------------------------------------------

# myStudents = list() ---Replace next line with this code, when project complete
myStudents = [Students("Jay", "Miles", 29), Students("Jon", "Barnett", 30), Students("Ben", "Hobbs", 28), Students("Sean", "Shearing", 32), Students("Will", "Price", 31)]
myClasses = ["Programming", "Maths", "English", "Science", "History"]

continueLoop = True #Sets my loop condition variable to True
while continueLoop == True: #Will loop this section of code until the variable condition is changed to false

    #Assign text to a list, ready to be passed into the RunMenu function
    menuList = ["------------Menu------------\n\n", "Register Student", "Assign Student to Class", "Take Register", "Exit"]

    #Triggers the RunMenu Function, with the list passed into it
    menuChoice = RunMenu(menuList)

    #This will be the If statement used to make a selection based on what the user has input in the menu function
    if menuChoice == 1:
        RegStudents(myStudents)
    elif menuChoice == 2:
        AssignStudents(myStudents, myClasses)
    elif menuChoice == 3:
        print("Take Register coming soon...")
    else:
        print("Goodbye!")
        continueLoop = False #Reassign the loop condition variable to false to break the loop and close the program