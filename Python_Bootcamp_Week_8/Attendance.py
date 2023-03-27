from Assign_Students import SelectSubject
from Generic_Functions import DisplayStudentsBySubject

def TakeAttendance(myClasses):

    subjectChoice = SelectSubject(myClasses)

    if subjectChoice != len(myClasses) + 1:

        subjectChoice = subjectChoice - 1
        DisplayStudentsBySubject(myClasses, subjectChoice)


