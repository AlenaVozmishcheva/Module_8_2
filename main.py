import re

class Teacher:

    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience

    def get_name(self):
        return f"{self.__name}"

    def get_education(self):
        return f"{self.__education}"

    def get_experience(self):
        return f"{self.__experience}"

    def set_experience(self, new_experience):
        if new_experience < 0:
            raise ValueError("Стаж работы не может быть отрицательным!")
        self.__experience = new_experience
        return f"Стаж работы изменен на {new_experience} лет"

    def get_data_teacher(self):
        data = f"Имя: {self.get_name()}, образование: {self.get_education()}, стаж: {self.get_experience()}"
        return data


    def add_mark(self, name_student, mark_student):
        self.__name_student = name_student
        self.__mark_student = mark_student
        return f"{self.get_name()} поставил оценку {self.__mark_student} студенту {self.__name_student}"

    def remove_mark(self, name_student, mark_student):
        self.__name_student = name_student
        self.__mark_student = mark_student
        return f"{self.get_name()} удалил оценку {self.__mark_student} студенту {self.__name_student}"

    def give_a_consultation(self, class_of_school):
        self.__class_of_school = class_of_school
        return f"{self.get_name()} провел консультацию в классе {self.__class_of_school} "


class DisciplineTeacher(Teacher):

    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self.__discipline = discipline
        self.__job_title = job_title

    def get_discipline(self):
        return f"{self.__discipline}"

    def get_job_title(self):
        return f"{self.__job_title}"

    def set_job_title(self, new_job_title):
        pattern = re.compile(r'^[A-Яа-я]+$')
        if not re.match(pattern, new_job_title):
            raise ValueError ("Некорректный ввод данных!")
        self.__job_title = new_job_title
        return f"Должность изменена на {new_job_title}"

    def get_data_teacher(self):
        data = super().get_data_teacher()
        return f"{data}\nПредмет {self.get_discipline()}, Должность: {self.get_job_title()}"

    def add_mark(self, name_student, mark_student):
        add = super().add_mark(name_student, mark_student)
        return f"{add}\nПредмет {self.__discipline}"

    def remove_mark(self, name_student, mark_student):
        remove = super().remove_mark(name_student, mark_student)
        return f"{remove}\nПредмет {self.__discipline}"


    def give_a_consultation(self, class_of_school):
        nom_of_class = super().give_a_consultation(class_of_school)
        return f"{nom_of_class}.\nПо предмету {self.get_discipline()} как {self.get_job_title()}"

teacher = Teacher('Иван Петров','БГПУ', '4')
print(teacher.get_data_teacher())
print(teacher.set_experience(1))
print()
print(teacher.add_mark('Петр Сидоров', '4'))
print()
print(teacher.remove_mark('Дмитрий Степанов', '3'))
print()
print(teacher.give_a_consultation('9Б'))
print()
teacher_1 = DisciplineTeacher('Иван Петров','БГПУ', '4', 'химия', 'директор')
print(teacher_1.get_data_teacher())
print()
print(teacher_1.add_mark('Иванов Николай', '4'))
print()
print(teacher_1.remove_mark('Сидоров Дмитрий', '3'))
print()
print(teacher_1.give_a_consultation('10Б'))
print(teacher_1.set_job_title('завуч'))

