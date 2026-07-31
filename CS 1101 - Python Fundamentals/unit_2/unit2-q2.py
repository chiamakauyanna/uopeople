# Construct Boolean expressions by extending your program to ask the user if they have any medical conditions (yes or no).
# If the user is 40 or older AND has a medical condition, print: "Medical clearance required before joining."
# If the user is under 40 OR has no medical condition, print: "You can proceed with registration."
# If the user enters an invalid response, print: "Invalid input. Please enter 'yes' or 'no'."



age = int(input("How old are you? "))

if (age < 18):
  print("You are eligible for the Teen Fitness Program.")
elif(age >= 18 and age < 40):
  print("You are eligible for the Regular Fitness Program.")
elif(age >= 40):
  print("You are eligible for the Senior Wellness Program.")
   
medical_condition = input("Do you have any medical condition (yes or no)? ").lower()

if (age >= 40 and medical_condition == 'yes'):
  print("Medical clearance required before joining.")
elif(age < 40 or medical_condition == 'no'):
  print("You can proceed with registration.")
else:
  print("Invalid input. Please enter 'yes' or 'no'.")