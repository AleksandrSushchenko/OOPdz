class Student:
    def __init__(self, name, surname, gender_st):
        self.name = name
        self.surname = surname
        self.gender_st = gender_st
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_st = {}

class Mentor:
    def __init__(self, name, surname,):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_lec = {}

class Lecturer(Mentor):
    def rate_lec(self, Lecturer, course, grade_lec):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_st:
                student.grades_st[course] += [grade_st]
            else:
                student.grades_st[course] = [grade_st]
        else:
            return 'Ошибка'

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade_st):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_st:
                student.grades_st[course] += [grade_st]
            else:
                student.grades_st[course] = [grade_st]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_Reviewer = Reviewer ('Вася', 'Пупкин')
cool_Reviewer.courses_attached += ['Python']

cool_Reviewer.rate_hw(best_student, 'Python', 10)
cool_Reviewer.rate_hw(best_student, 'Python', 10)
cool_Reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades_st)