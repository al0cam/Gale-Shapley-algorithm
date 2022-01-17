def createPriorityList(student, studentList):
        list = []
        
        for index, i in enumerate(studentList):
            if i['Redni broj'] == student.get('Redni broj'):
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

    
    