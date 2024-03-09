class Student:
    students = []

    def add_student(self):
        self.studentID = int(input('Enter student ID: '))
        self.name = input("Enter Student name: ")
        self.age = int(input("Enter Student age: "))
        self.averageScore = int(input("Enter Student average score: "))

        students.append({
            'ID': self.studentID,
            'name': self.name,
            'age': self.age,
            'avereageScore': self.averageScore
        })

    def print_student_into(self):
        return {
            'ID': self.studentID,
            'name': self.name,
            'age': self.age,
            'avereageScore': self.averageScore
        }

    # def find_student(self):
