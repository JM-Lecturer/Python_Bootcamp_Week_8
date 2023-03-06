from Register_Classes import (Students,Classes)
from Generic_Functions import RunMenu
import Register_Students as Reg, Assign_Students as Agn

def Main():
    # myStudents = list() ---Replace next line with this code, when project complete
    myStudents = [Students("Jay", "Miles", 29), Students("Jon", "Barnett", 30), Students("Ben", "Hobbs", 28), Students("Sean", "Shearing", 32), Students("Will", "Price", 31)]
    myClasses = [Classes("Programming"), Classes("Maths"), Classes("English"), Classes("Science"), Classes("History")]



    #Delete THIS WHEN FINISHED teaching---------------------------------------------------------

    myClasses[0].classStudents.append(myStudents[0])
    del myStudents[0]
    print(myClasses[0].classStudents[0].GetName())

    input("[STOP HERE]")

    #Delete THIS WHEN FINISHED teaching---------------------------------------------------------

    continueLoop = True #Sets my loop condition variable to True
    while continueLoop == True: #Will loop this section of code until the variable condition is changed to false

        #Assign text to a list, ready to be passed into the RunMenu function
        menuList = ["------------Menu------------\n\n", "Register Student", "Assign Student to Class", "Take Register", "Exit"]

        #Triggers the RunMenu Function, with the list passed into it
        menuChoice = RunMenu(menuList)

        #This will be the If statement used to make a selection based on what the user has input in the menu function
        if menuChoice == 1:
            Reg.RegStudents(myStudents)
        elif menuChoice == 2:
            Agn.AssignStudents(myStudents, myClasses)
        elif menuChoice == 3:
            print("Take Register coming soon...")
        else:
            print("Goodbye!")
            continueLoop = False #Reassign the loop condition variable to false to break the loop and close the program

Main()