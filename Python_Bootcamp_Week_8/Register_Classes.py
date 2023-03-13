class ValueOutOfRange(Exception):
    #This class is for triggering a custom exception
    pass

class Students(): #Class template for student objects

    #These are the member attributes/variables to define our object
    firstName = ""
    secondName = ""
    age = 0
    Attendance = False

    def __init__(self, firstName, secondName, age): #Constructor used to initialize our student objects

        self.firstName = firstName
        self.secondName = secondName
        self.age = age

    def GetName(self): #Member function, simply returns a concat string of the students name

        return self.firstName + " " + self.secondName

class Subjects():
    
    className = ""
    classStudents = list()

    def __init__(self, className):

        self.className = className
        self.classStudents = list()



