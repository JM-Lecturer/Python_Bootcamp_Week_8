from Register_Classes import Students

def SaveStudentDetails(outputStudents, fileName):
    
    s = open(fileName + ".txt", "wt")

    for student in outputStudents:

        s.write(student.firstName + "\n")
        s.write(student.secondName + "\n")
        s.write(str(student.age) + "\n")

    s.close()

def LoadStudentDetails(fileName):

    inputStudents = list()

    s = open(fileName + ".txt", "r")

    for line in s:

        a = line
        b = s.readline()
        c = s.readline()
        inputStudents.append(Students(a, b, int(c)))

    s.close()

    return inputStudents