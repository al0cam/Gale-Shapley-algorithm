from time import sleep
from typing import List
import Conwerther as cw
import Faculty
import Student

def findFaculty(faculty, facultyArray: List[Faculty.Faculty]):
    for i in facultyArray:
        if(i.name == faculty.get('studij')):
            return i

studentList = cw.excelToJson('MS_prijave_2021_prvi_rok.xlsx')
facultyList = cw.excelToJson('MS_prijave_2021_prvi_rok.xlsx','Kvote')


studentArray = []
for i in studentList:
    prioList =  Student.createPriorityList(i, studentList)
    studentObject = Student.Student(i, prioList)
    studentArray.append(studentObject)

facultyArray = []
for i in facultyList:
    facultyObject = Faculty.Faculty(i.get('Diplomski studij'), i.get('Kvota'))
    facultyArray.append(facultyObject)

while studentArray:
    student = studentArray.pop(0)
    while student.priorityList:
        faculty = student.priorityList.pop(0)
        facultyObject = findFaculty(faculty, facultyArray)
        
        student.getPlace(faculty)
        facultyObject.sortAcceptedStudents()

        if(facultyObject.willAcceptStudent(student)):
            removedStudent = facultyObject.acceptStudent(student)
            facultyObject.sortAcceptedStudents()

            if(removedStudent):
                removedStudent.points = 0
                removedStudent.faculty = ''
                studentList.append(removedStudent)
            break


dictionary = dict()
for i in facultyArray:
    dictKid = []
    for index, s in enumerate(i.acceptedStudents):
        row = {

                "index": index,
                "student": s.number,
                "points": s.points
            }
        dictKid.append(row)
        # print(f"{index}: \tnumber: {s.number}, points: {s.points}, faculty: {s.currentFaculty}" )
    dictionary[i.name]= dictKid
