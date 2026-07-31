students = ["Alice", "Ben", "Chloe", "David"]

for student in students:
  print(student)
  
students_grade = []

while True:
  grade = input("Enter students' grade. ").lower()

  if grade == 'done':
    break 
  
  try:
   grade = int(grade)
  except ValueError:
    continue
    
  if grade < 0:
    continue
   
  students_grade.append(grade)

print(students_grade)

classes = [["Alice", "Ben"], ["Chloe", "David"]]
class_num = 1

for class_list in classes:
  print("Students in class", class_num)
  for student_name in class_list:
    print(student_name)
  class_num = class_num + 1