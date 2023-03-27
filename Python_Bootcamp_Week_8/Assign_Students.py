import Generic_Functions as Fun

def SelectSubject(myClasses):

    menuList = ["Which subject would you like to assign students into?\n"]
    for x in range(0, len(myClasses)):
        menuList.append(myClasses[x].className)
    menuList.append("Return to Menu")

    choice = Fun.RunMenu(menuList)

    return choice

def AssignStudents(myStudents, myClasses):

    print("\n------------Assign Students------------\n\n")
    subjectChoice = SelectSubject(myClasses)

    if subjectChoice != len(myClasses) + 1:

        subjectChoice = subjectChoice - 1

        continueLoop = True
        while continueLoop == True:
    
            Fun.DisplayStudentsBySubject(myClasses, subjectChoice, True)
            Fun.DisplayAllStudents(myStudents)

            studentChoice = Fun.StudentSelectionMenu(myStudents, "------------Assign Students------------", "Which student would you like to assign to a class?")
            
            if studentChoice == len(myStudents) + 1:
                continueLoop = False
            else:

                myClasses[subjectChoice].classStudents.append(myStudents[studentChoice - 1])
                del myStudents[studentChoice - 1]

                print("\n\nYou have successfully added " + myClasses[subjectChoice].classStudents[len(myClasses[subjectChoice - 1].classStudents) - 1].GetName() + " to the " + myClasses[subjectChoice].className + " class!")
                input("[Press Enter to Continue]")
                    
                    
