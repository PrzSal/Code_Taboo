class Student:
    list_student = []

    def __init__(self, student):
        self.student = student
        __class__.list_student.append(self)

    def __str__(self):
        return self.student
