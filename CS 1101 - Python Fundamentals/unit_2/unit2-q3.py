# Implement Nested Conditional statements by extending your program. SmartFit offers two types of membership: Basic and Premium.
# Ask the user to choose a membership type.
# If the user selects Basic, ask if they want personal training (yes/no):
# If yes, print: "Basic plan with personal training: $45 per month."
# If no, print: "Basic plan: $30 per month."
# If the user selects Premium, print: "Premium plan: $60 per month."

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
elif(medical_condition != "yes" and medical_condition != "no"):
  print("Invalid input. Please enter 'yes' or 'no'.")
  
membership_type = input("Choose a membership type (basic or premium). ").lower() 
 
if (membership_type == "basic"):
  personal_training = input("Do you want personal training (yes or no)? ")
  if (personal_training == 'yes'):
    print("Basic plan with personal training: $45 per month.")
  elif (personal_training == 'no'):
    print("Basic plan: $30 per month.")
  else:
    print("Invalid input. Please enter 'yes' or 'no'.")
elif (membership_type == "premium"):
  print("Premium plan: $60 per month.")
else:
  print("Invalid input. Please enter 'Basic' or 'Premium'.")