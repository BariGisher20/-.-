class Student:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}

  def add_some(self, course):
    if course:
      self.courses_in_progress.append(course)     

  def add_some_foo(self, course, mark):
    if mark:
      self.grades[course] = mark

  def average_grades(self):
    st_grades=[]
    for st_grades_list in self.grades.values():
      for grade in st_grades_list: 
        st_grades.append(grade)
    grades_sum=sum(st_grades)
    average_grade=grades_sum/len(st_grades)
    return round(average_grade, 2)
  
  def __str__(self):
    for finished in self.finished_courses:
      for progress in self.courses_in_progress:
        res_student = f'Имя = {self.name}  \nФамилия = {self.surname} \nСредняя оценка за лекции = {self.average_grades()} \nКурсы в процессе изучения: {progress} \nЗавершенные курсы: {finished}'
    return res_student
  
  def __lt__(self, other):
    if not isinstance(other, Student):
      print('На наших курсах нет студента с такими ФИО')
      return
    return self.average_grades() < other.average_grades()  

class Mentor:

  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []
        
class Lecturer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.course_name=[]
    self.grades_lec=[]
    self.course_grade= {}

  def rate_lec(self, lecturer, course, grade, student):
    if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in student.courses_in_progress:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]
      else:
        lecturer.grades[course] = [grade]
    else:
      return 'Ошибка'

  def add_some(self, mark):
    if mark:
      self.grades_lec.append(mark)
            
  def add_some_foo(self, course, mark):
    if mark:
      self.course_grade[course] = mark

  def average_grades(self):
    lec_grades=[]
    for lec_grades_list in self.course_grade.values():
      for grade in lec_grades_list: 
        lec_grades.append(grade)
    grades_sum=sum(lec_grades)
    average_grade=grades_sum//len(lec_grades)
    return average_grade
  
  def __str__(self):
    res_lecturer = f'Имя = {self.name}  \nФамилия = {self.surname} \nСредняя оценка за лекции = {self.average_grades()}'
    return res_lecturer
  def __lt__(self, other):
    if not isinstance(other, Lecturer):
      print('На наших курсах нет преподавателя с такими ФИО')
      return
    return self.average_grades() < other.average_grades()
  
class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in student.grades:
        student.grades[course] += [grade]
      else:
        student.grades[course] = [grade]
    else:
      return 'Ошибка'
  def __str__(self):
    res_reviewer = f'Имя = {self.name}  \nФамилия = {self.surname}'
    return res_reviewer

#CODE REALIZATION
#REVIEWER
some_reviewer=Reviewer('Кора', 'Кроули')
print(some_reviewer)

#STUDENT
student_list=[]
samvel_tarley=Student('Семвел', 'Тарли', 'man')
samvel_tarley.finished_courses.append('Html, ''JS')
samvel_tarley.add_some('Python, ' 'CSS')
samvel_tarley.add_some_foo('Python', [10,10,8])
samvel_tarley.average_grades()
student_list.append((samvel_tarley.name +' '+samvel_tarley.surname))
print(samvel_tarley)

sansa_stark=Student('Санса', 'Старк', 'woman')
sansa_stark.finished_courses.append('CSS, ''JS')
sansa_stark.add_some('Python, ' 'HTML')
sansa_stark.add_some_foo('Python', [10,10,9])
sansa_stark.average_grades()
student_list.append((sansa_stark.name +' '+sansa_stark.surname))
print(sansa_stark)

print(samvel_tarley < sansa_stark)

def average_student_grade(student_list, course_name):
  for student in student_list:
    if course_name in Student.courses_in_progress:
      if course_name in Student.grades:
        all_st_average_grades=[] 
        avg_st = sum(student.grades.get(course_name)) / len(student.grades.get(course_name))
        all_st_average_grades.append(avg_st)
        all_avg_st = sum(all_st_average_grades) / len(all_st_average_grades)
        res = print(f'Средний балл студента по курсу {course_name} = {round(all_avg_st, 2)}')
        return res

#LECTURER
lecturer_list=[]
john_snow=Lecturer('Джон', 'Сноу')
john_snow.add_some([10,10,10])
john_snow.add_some_foo('Python', [10,10,10])
john_snow.average_grades()
lecturer_list.append((john_snow.name +' '+john_snow.surname))
print()

cersei_lannister=Lecturer('Серсея', 'Ланнистер')
cersei_lannister.add_some([10,9,9])
cersei_lannister.add_some_foo('Python', [10,9,9])
cersei_lannister.average_grades()
lecturer_list.append((cersei_lannister.name +' '+cersei_lannister.surname))
print(cersei_lannister)

print(cersei_lannister < john_snow)


def average_lecturer_grade(lecturer_list, course_name):
  for lecturer in lecturer_list:
    if course_name in Lecturer.courses_attached:
      if course_name in Lecturer.course_grade:
        all_lec_average_grades=[] 
        avg = sum(lecturer.course_grade.get(course_name)) / len(lecturer.course_grade.get(course_name))
        all_lec_average_grades.append(avg)
        all_avg_lec = sum(all_lec_average_grades) / len(all_lec_average_grades)
        res = print(f'Средний балл за лекции по курсу {course_name} = {round(all_avg_lec, 2)}')
        return res