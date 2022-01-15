
from operator import index, indexOf

from numpy import sort


def createPriorityList(student, studentList):
        list = []
        # list.append(
        #     {
        #         "prioritet": student.get("Prioritet"),
        #         'studij': student.get("Diplomski studij"),
        #         'sukladnost': student.get("Sukladnost"),
        #         'ukupno': student.get("UKUPNO (prosjek x 100 + sukladnost)")
        #     }
        # )
        for index, i in enumerate(studentList):
            if i['Redni broj'] == student.get('Redni broj'):
                # print(indexOf(studentList, i))
                # print(i)
                list.append(
                    {
                        'prioritet': int(i.get("Prioritet")),
                        'studij': i.get("Diplomski studij"),
                        'sukladnost': i.get("Sukladnost"),
                        'ukupno': float(i.get("UKUPNO (prosjek x 100 + sukladnost)"))
                    }
                )
                studentList.pop(index)

        list = sorted(list,key=lambda x:x.get('prioritet'))
        return list




class Student:
    number = -1
    priorityList = []
    gradeAverage = 0
    currentFaculty = ''
    points = 0

    def getPlace(self, faculty):
        self.points = faculty.get('ukupno')
        self.currentFaculty = faculty.get('studij')

    def __init__(self, student, priorityList):
        self.number = student['Redni broj']
        self.gradeAverage = student['Prosjek ocjena preddiplomskog studija']
        self.priorityList = priorityList

    
    