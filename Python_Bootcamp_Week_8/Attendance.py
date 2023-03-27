from Assign_Students import SelectSubject
from Generic_Functions import (DisplayStudentsBySubject, StudentSelectionMenu)

def TakeAttendance(myClasses):

    subjectChoice = SelectSubject(myClasses)

    if subjectChoice != len(myClasses) + 1:

        subjectChoice = subjectChoice - 1

        continueLoop = True
        while continueLoop == True:

            DisplayStudentsBySubject(myClasses, subjectChoice, False)

            studentSelection = StudentSelectionMenu(myClasses[subjectChoice].classStudents, "----------Take Attendance----------", "Select a Student:")

            if studentSelection != len(myClasses[subjectChoice].classStudents) + 1:

                if myClasses[subjectChoice].classStudents[studentSelection - 1].attendance == False:

                    myClasses[subjectChoice].classStudents[studentSelection - 1].attendance = True

                else:

                    myClasses[subjectChoice].classStudents[studentSelection - 1].attendance = False

            else:

                continueLoop = False