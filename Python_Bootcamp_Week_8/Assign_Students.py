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

                menuList = ["\n\nWhich class wouild you like to assign " + myStudents[studentChoice - 1].GetName() + " to:\n"]
                for x in range(0, len(myClasses)):
                    menuList.append(myClasses[x])
                menuList.append("Return")

                classChoice = RunMenu(menuList)

                if classChoice == len(menuList) - 1:

                    classLoop = False

                else:

                    classLoop = False
                    myStudents[studentChoice - 1].className = myClasses[classChoice - 1]
                    print("\n\nYou have successfully added " + myStudents[studentChoice - 1].GetName() + " to the " + myStudents[studentChoice - 1].className + " class!")
                    input("[Press Enter to Continue]")
