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
        for e in range(0, len(Grades)):
            total2 = total2 + Grades[e]
        if total2 >= 86:
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

    def showGrade(coursebool):
        if coursebool == 1:
            print(Grades[0])
        elif coursebool == 2:
            print(Grades[1])
        elif coursebool == 3:
            print(Grades[2])
        elif coursebool == 4:
            print(Grades[3])
        elif coursebool == 5:
            print(Grades[4])
        elif cousebool == 6:
            print(Grades[5])
        elif cousebool == 7:
            print(Grades[6])

    def __del__(self):
        pass

    def average(self):
        for i in range(0, len(Grades)):
            total = total + Grades[i]
        ave = total / len(Grades)
        print("Your average is "+ave)

def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox","12346", 11)
    st1.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st1.getGrades( [71, 98, 93, 95, 68, 81, 71])



