class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.zakonch_kurs = []
        self.kurs_v_processe = []
        self.ocenka = {}
        self.sred_dz = []

    def post_ocenku_lectoru(self, lector, kurs, ocenka_lectoru):
        if isinstance(lector, Lecturer) and kurs in self.kurs_v_processe:
            if kurs in lector.ocenka_lectoru:
                lector.ocenka_lectoru[kurs] += [ocenka_lectoru]
            else:
                lector.ocenka_lectoru[kurs] = [ocenka_lectoru]
        else:
            return "error"

    def sred_ocenka_dz(self):
        self.sred_dz = sum(self.ocenka['Phyton'])/len(self.ocenka['Phyton'])
        return self.sred_dz

    def __str__(self):
        return f'Имя:{self.name}\n' \
               f'Фамилия:{self.surname}\n' \
               f'Средняя оценка за дз: {self.sred_ocenka_dz()}\n'\
               f'Курсы в процессе изучения: {",".join(self.kurs_v_processe)}\n'\
               f'Завершенные курсы: {",".join(self.zakonch_kurs)}\n'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return student_1.sred_dz < student_2.sred_dz


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.pricrepl_kurs = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.ocenka_lectoru = {}
        self.sred_ph = []

    def sred_ocenka_lect(self):
        self.sred_ph = sum(self.ocenka_lectoru['Phyton'])/len(self.ocenka_lectoru['Phyton'])
        return self.sred_ph

    def __str__(self):
        return f'Имя:{self.name}\n' \
               f'Фамилия:{self.surname}\n' \
               f'Средняя оценка за лекции: {self.sred_ocenka_lect()}\n'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return lector_1.sred_ph > lector_2.sred_ph


class Reviewer (Mentor):
    def post_ocenku_stud(self, student, kurs, ocenka):
        if isinstance(student, Student) and kurs in self.pricrepl_kurs and kurs in student.kurs_v_processe:
            if kurs in student.ocenka:
                student.ocenka[kurs] += [ocenka]
            else:
                student.ocenka[kurs] = [ocenka]
        else:
            return 'error' \


    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n'


student_1 = Student('Петр', 'Иванов', 'М')
student_1.kurs_v_processe += ['Phyton']
student_1.zakonch_kurs += ['Введение в програмирование']

student_2 = Student('Михайл', 'Михалыч', 'М')
student_2.kurs_v_processe += ['Phyton']
student_2.zakonch_kurs += ['Введение в програмирование']


lector_1 = Lecturer('Алексей', 'Петрович')
lector_1.pricrepl_kurs += ['Phyton']


lector_2 = Lecturer('Ксенья', 'Петровна')
lector_2.pricrepl_kurs += ['Phyton']

prover_1 = Reviewer('Николай', 'Опарин')
prover_1.pricrepl_kurs += ['Phyton']

prepod_1 = Reviewer('Татьяна', 'Петровна')
prepod_1.pricrepl_kurs += ['Phyton']

student_1.post_ocenku_lectoru(lector_1, 'Phyton', 10)
student_1.post_ocenku_lectoru(lector_1, 'Phyton', 10)
student_1.post_ocenku_lectoru(lector_1, 'Phyton', 10)

student_1.post_ocenku_lectoru(lector_2, 'Phyton', 9)
student_1.post_ocenku_lectoru(lector_2, 'Phyton', 8)
student_1.post_ocenku_lectoru(lector_2, 'Phyton', 7)


prepod_1.post_ocenku_stud(student_1, 'Phyton', 8)
prepod_1.post_ocenku_stud(student_1, 'Phyton', 7)
prepod_1.post_ocenku_stud(student_1, 'Phyton', 9)

prepod_1.post_ocenku_stud(student_2, 'Phyton', 10)
prepod_1.post_ocenku_stud(student_2, 'Phyton', 10)
prepod_1.post_ocenku_stud(student_2, 'Phyton', 10)


print(prover_1)
print(student_1)
print(student_2)
print(student_1.sred_dz > student_2.sred_dz)
print(lector_1)
print(lector_2)
print(lector_1.sred_ph > lector_2.sred_ph)
