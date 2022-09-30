class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.zakonch_kurs = []
        self.kurs_v_processe = []
        self.ocenka = {}
    def post_ocenku_lectoru (self, lector, kurs, ocenka_lectoru):
        if isinstance(lector, Lecturer) and kurs in self.kurs_v_processe:
            if kurs in lector.ocenka_lectoru:
                lector.ocenka_lectoru[kurs] += [ocenka_lectoru]
            else:
                lector.ocenka_lectoru[kurs] = [ocenka_lectoru]
        else:
            return "error"
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.pricrepl_kurs = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.ocenka_lectoru = {}

class Reviewer (Mentor):
    def post_ocenku_stud(self,student, kurs, ocenka):
        if isinstance(student, Student) and kurs in self.pricrepl_kurs and kurs in student.kurs_v_processe:
            if kurs in student.ocenka:
                student.ocenka[kurs] += [ocenka]
            else:
                student.ocenka[kurs] = [ocenka]
        else:
            return 'error'

student_1 = Student('Pety','Ivanov','M')
student_1.kurs_v_processe += ['Phyton']

lector_1 = Lecturer('Petr','Petrovich')
lector_1.pricrepl_kurs += ['Phyton']

student_1.post_ocenku_lectoru(lector_1, 'Phyton', 3)
student_1.post_ocenku_lectoru(lector_1, 'Phyton', 3)
student_1.post_ocenku_lectoru(lector_1, 'Phyton', 3)

print(lector_1.ocenka_lectoru)

prepod_1 = Reviewer('Taisa','Orlova')
prepod_1.pricrepl_kurs += ['Phyton']

prepod_1.post_ocenku_stud(student_1, 'Phyton', 8)
prepod_1.post_ocenku_stud(student_1, 'Phyton', 7)
prepod_1.post_ocenku_stud(student_1, 'Phyton', 9)

print(student_1.ocenka)