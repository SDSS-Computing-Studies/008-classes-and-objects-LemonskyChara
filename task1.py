#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grade - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:

    # properties should be listed first

    def __init__(self, name, studentNumber, grade): # You will need to create your own input parameters for all methods
        self.name = name
        self.studentNumber = studentNumber
        self.grade = grade

    def getCourses(self, lista):
        global Courses
        Courses = []
        Courses = lista
        return Courses

    def getGrades(self, listb):
        global Grades
        Grades = []
        Grades = listb
        return Grades

    def getHonorRoll(self):
        b = 0
        for e in range(0, len(Grades)):
            b = b + Grades[e]
        if b >= 86:
            return True
        else:
            return False
        

    def showCourses(self):
        print("---------------------")
        print("Choose one course you want to know: ")
        print("1." + Courses[0])
        print("2." + Courses[1])
        print("3." + Courses[2])
        print("4." + Courses[3])
        print("5." + Courses[4])
        print("6." + Courses[5])
        print("7." + Courses[6])
        coursebool = input("Choose a number[1-7]: ")
        print("")
        return int(coursebool)

    def showGrade(self, coursebool):
        if coursebool == 1:
            print("Your mark is " + str(Grades[0]))
        elif coursebool == 2:
            print("Your mark is " + str(Grades[1]))
        elif coursebool == 3:
            print("Your mark is " + str(Grades[2]))
        elif coursebool == 4:
            print("Your mark is " + str(Grades[3]))
        elif coursebool == 5:
            print("Your mark is " + str(Grades[4]))
        elif coursebool == 6:
            print("Your mark is " + str(Grades[5]))
        elif coursebool == 7:
            print("Your mark is " + str(Grades[6]))

    def __del__(self):
        print(self.name + " Goodbye.")

    def average(self):
        a = 0
        for i in range(0, len(Grades)):
            a = a + Grades[i]
        ave = float(a / len(Grades))
        ave = round(ave, 1)
        return float(ave)

def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox","12346", 11)
    st1.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st1.getGrades( [71, 98, 93, 95, 68, 81, 71])


main()

