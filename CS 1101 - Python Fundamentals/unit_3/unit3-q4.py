# Write a short code example that prints all student names organized by class. After that, explain why using a nested loop is useful or not in this situation.
# Below is a name list organized by class example. Use the list to complete your code:


classes = [["Alice", "Ben"], ["Chloe", "David"]]
class_num = 1

# iterate over list of classes
for class_list in classes:
  print("Students in class", class_num)
  for student_name in class_list:
    print(student_name)
  class_num = class_num + 1
  
  