from Register_Classes import (Students,Subjects)
from Generic_Functions import RunMenu
import Register_Students as Reg, Assign_Students as Agn, Attendance as Att

def Main():
    # myStudents = list() ---Replace next line with this code, when project complete
    myStudents = [Students("Jay", "Miles", 29), Students("Jon", "Barnett", 30), Students("Ben", "Hobbs", 28), Students("Sean", "Shearing", 32), Students("Will", "Price", 31)]
    myClasses = [Subjects("Programming"), Subjects("Maths"), Subjects("English"), Subjects("Science"), Subjects("History")]

    myClasses[0].classStudents.append(Students("Greg","Smith", 19))
    myClasses[0].classStudents.append(Students("Jane","Jameson", 21))
    myClasses[0].classStudents.append(Students("Alice","Parker", 32))
    myClasses[0].classStudents.append(Students("Meg","Kent", 22))
    myClasses[0].classStudents.append(Students("Bob","Martinson", 18))
    myClasses[0].classStudents.append(Students("Frank","Wallace", 23))
    
    myClasses[1].classStudents.append(Students("Mike","Duke", 19))
    myClasses[1].classStudents.append(Students("Ben","Vik", 21))
    myClasses[1].classStudents.append(Students("Derek","Pop", 32))
    myClasses[1].classStudents.append(Students("Sophie","Yasmar", 22))
    myClasses[1].classStudents.append(Students("Alicia","Gundarson", 18))
    myClasses[1].classStudents.append(Students("Mandy","Reiksmen", 23))

    #-------------------------------------------------------------------------------------------------------------------------------

    continueLoop = True #Sets my loop condition variable to True
    while continueLoop == True: #Will loop this section of code until the variable condition is changed to false

        #Assign text to a list, ready to be passed into the RunMenu function
        menuList = ["------------Menu------------\n\n", "Register Student", "Assign Student to Class", "Take Attendance", "Exit"]

        #Triggers the RunMenu Function, with the list passed into it
        menuChoice = RunMenu(menuList)

        #This will be the If statement used to make a selection based on what the user has input in the menu function
        if menuChoice == 1:
            Reg.RegStudents(myStudents)
        elif menuChoice == 2:
            Agn.AssignStudents(myStudents, myClasses)
        elif menuChoice == 3:
            Att.TakeAttendance(myClasses)
        else:
            print("Goodbye!")
            continueLoop = False #Reassign the loop condition variable to false to break the loop and close the program

Main()