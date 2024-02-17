class Employee:
    def __init__(self, ID, name, age, dateOfBirth, workDay, placeOfOrigin):
        self.ID = ID
        self.name = name
        self.age = age
        self.dateOfBirth = dateOfBirth
        self.workDay = workDay
        self.placeOfOrigin = placeOfOrigin
        self.salaryRank = 4.2


class Manager(Employee):
    def __init__(self, ID, name, age, dateOfBirth, workDay, placeOfOrigin):
        super().__init__(selfy, ID, name, age, dateOfBirth, workDay, placeOfOrigin)
        self.position = "Manger"
        self.salaryRank = 5.0


class Director:
    def __init__(self, ID, name, dateOfBirth, workDay, placeOfOrigin):
        super()__init__(selfy, ID, name, dateOfBirth, workDay, placeOfOrigin)
        self.position = "Director"
        self.salaryRank = 7.0
