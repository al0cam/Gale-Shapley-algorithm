
from operator import indexOf
from typing import ChainMap
from unicodedata import numeric

class Faculty:
    name = ''
    size = 0
    acceptedStudents = []

    def __init__(self, name, size):
        self.size = size
        self.name = name

    def sortAcceptedStudents(self):
        self.acceptedStudents = sorted(self.acceptedStudents, key=lambda x:x.points, reverse=True )

    def acceptStudent(self, student):
        removedStudent = False
        if self.isFull():
            removedStudent = self.acceptedStudents.pop()
        
        if not self.isFull() or self.isRankedBetterThan(student, removedStudent):
            self.acceptedStudents.append(student)
        else:
            self.acceptedStudents.append(student)
        return removedStudent

    def isStudentAlreadyAccepted(self, student):
        for i in self.acceptedStudents:
            if student.number == i.number:
                return True
        return False

    def willAcceptStudent(self, student):
        if not self.isStudentAlreadyAccepted(student):
            if not self.isFull():
                return True
            elif self.isRankedBetterThan(student, (self.acceptedStudents[-1])):
                return True
        return False

    def isRankedBetterThan(self, student1, student2):
        return student1.points > student2.points
    
    def isFull(self):
        return self.size <= len(self.acceptedStudents)
