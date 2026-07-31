# Discuss how you would use a while loop to repeatedly ask the teacher to enter students’ grades until they type "done". Provide a short example to demonstrate your approach.

students_grade = []

while True:
  grade = input("enter students' grade ")
  if grade == 'done':
    break
  students_grade.append(grade)

print(students_grade)