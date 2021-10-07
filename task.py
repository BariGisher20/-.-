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
        


meri_crawley=Student('Мэри', 'Кроули', 'woman')
meri_crawley.finished_courses.append('Html, ''JS')
meri_crawley.add_some('Python, ' 'CSS')
meri_crawley.add_some_foo('Python', [10,10,8])
meri_crawley.average_grades()
print(meri_crawley)

edith_crawley=Student('Эдит', 'Кроули', 'woman')
edith_crawley.finished_courses.append('CSS, ''JS')
edith_crawley.add_some('Python, ' 'HTML')
edith_crawley.add_some_foo('Python', [10,10,9])
edith_crawley.average_grades()
print(edith_crawley)
print(meri_crawley < edith_crawley)


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
  
robert_crawley=Lecturer('Роберт', 'Кроули')
robert_crawley.add_some([10,10,10])
robert_crawley.add_some_foo('Python', [10,10,10])
robert_crawley.average_grades()
print(robert_crawley)
john_bates=Lecturer('Роберт', 'Кроули')
john_bates.add_some([10,9,9])
john_bates.add_some_foo('Python', [10,9,9])
john_bates.average_grades()
print(john_bates)
print(john_bates < robert_crawley)

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


some_reviewer=Reviewer('Кора', 'Кроули')
print(some_reviewer)


