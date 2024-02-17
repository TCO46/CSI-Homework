class Student:
    def __init__(self, name, age, address, origin, mathScore, physicScore, chemistryScore):
        self.name = name
        self.age = age
        self.address = address
        self.origin = origin
        self.mathScore = mathScore
        self.physicScore = physicScore
        self.chemistryScore = chemistryScore

    def getStudentAge(self):
        return self.age

    def getAverageScore(self):
        return round((self.mathScore + self.physicScore + self.chemistryScore) / 3, 2)

    def getStudentStatus(self):
        if self.getAverageScore() >= 8 and self.mathScore >= 6 and self.physicScore >= 6 and self.chemistryScore >= 6:
            return "Gioi"
        elif self.getAverageScore() >= 6.5 and self.mathScore >= 5 and self.physicScore >= 5 and self.chemistryScore >= 5:
            return "Kha"
        elif self.getAverageScore() >= 5 and self.mathScore >= 4 and self.physicScore >= 4 and self.chemistryScore >= 4:
            return "Trung Binh"
        else:
            return "Yeu"


testStudent = Student("Nguyen Van B", 2007, "Ha Noi", "Thai Binh", 6, 9, 7)
print(testStudent.getStudentAge())
print(testStudent.getAverageScore())
print(testStudent.getStudentStatus())
