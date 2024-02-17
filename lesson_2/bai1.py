class Student:
    def insert_student(self):
        self.ID = int(input('Enter student ID: '))
        self.full_name = input('Enter student name: ')
        self.age = int(input('Enter student age: '))
        self.score = float(input('Enter student score: '))

    def student_info(self):
        return {
            'ID': self.ID,
            'full_name': self.full_name,
            'age': self.age,
            'score': self.score
        }


student_a = Student()
student_a.insert_student()

student_b = Student()
student_b.insert_student()

print(student_a.student_info())
print(student_b.student_info())
