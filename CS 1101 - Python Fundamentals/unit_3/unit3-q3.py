# Incorporate a short code snippet that handles cases where a teacher might accidentally enter an invalid grade (like a negative number) or decide to stop entering grades early:
# Demonstrate how you would use:
# A break statement to stop entering grades completely.
# A continue statement to skip invalid grades (e.g., negative numbers) and move to the next input.

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

# store average grade
avg = 0

# calculate average
for grades in students_grade:
  avg += grades
avg /= len(students_grade)
print("Average score", avg)