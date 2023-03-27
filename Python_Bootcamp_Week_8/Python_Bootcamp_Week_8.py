from Register_Classes import (Students,Subjects)
from Generic_Functions import RunMenu
import Register_Students as Reg, Assign_Students as Agn, Attendance as Att
from IO_Functions import LoadStudentDetails

def Main():

    myStudents = LoadStudentDetails("UnassignedStudents")
    myClasses = [Subjects("Programming"), Subjects("Maths"), Subjects("English"), Subjects("Science"), Subjects("History")]

    myClasses[0].classStudents = LoadStudentDetails("ProgrammingStudents")
    myClasses[1].classStudents = LoadStudentDetails("MathsStudents")
    #myClasses[2].classStudents = LoadStudentDetails("EnglishStudents")
    #myClasses[3].classStudents = LoadStudentDetails("ScienceStudents")
    #myClasses[4].classStudents = LoadStudentDetails("HistoryStudents")

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