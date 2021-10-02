

class Student:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}

        
class Mentor:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []
        
class Lecturer(Mentor):
  def __init__(self, name, surname):
    self.course_name=''
    self.grades_lec=[]
    self.course_grade= {
  'PY': [10,10,10],
  'CSS': [10,10,10],
  'JS': [10,10,10]
  }
  def rate_lec(self, lecturer, course, grade, student):
    if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in student.courses_in_progress:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]
      else:
        lecturer.grades[course] = [grade]
    else:
      return 'Ошибка'
  def average_grade(self):
    res= list(self.course_grade['PY']+self.course_grade['CSS']+self.course_grade['JS'])
    grades_sum=sum(res)
    average_grade=grades_sum//len(res)
    return average_grade

class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in student.grades:
        student.grades[course] += [grade]
      else:
        student.grades[course] = [grade]
    else:
      return 'Ошибка'


teacher_1=Lecturer('Elena', 'Mitus')
# teacher_1.course_grade.setdefault('course_name', []).append([9,9,9])
res_1= teacher_1.average_grade()
print(res_1)