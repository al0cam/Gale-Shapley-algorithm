
import json
from time import sleep
from typing import List
import Conwerther as cw
import Faculty
import Student


studentList = cw.excelToJson('MS_prijave_2021_prvi_rok.xlsx')
facultyList = cw.excelToJson('MS_prijave_2021_prvi_rok.xlsx','Kvote')

def findFaculty(faculty, facultyArray: List[Faculty.Faculty]):
    for i in facultyArray:
        if(i.name == faculty.get('studij')):
            return i

studentArray = []
for i in studentList:
    prioList =  Student.createPriorityList(i, studentList)
    studentObject = Student.Student(i, prioList)
    studentArray.append(studentObject)

facultyArray = []
for i in facultyList:
    facultyObject = Faculty.Faculty(i.get('Diplomski studij'), i.get('Kvota'))
    facultyArray.append(facultyObject)

for i in studentArray:
    print(i.number)

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

        
# for i in facultyArray:
#     print(i.name)
#     for index, s in enumerate(i.acceptedStudents):
#         print(f"{index}: \tnumber: {s.number}, points: {s.points}, faculty: {s.currentFaculty}" )


for i in facultyArray:

    print(json.dumps(i.__dict__))