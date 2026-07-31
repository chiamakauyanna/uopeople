# Implement Nested Conditionals with logical operators to your existing program.
# If the user has Premium membership and their age is under 30, print: "You qualify for a youth discount! 10% off your plan."
# If the user has Basic membership and does not want personal training, print: "Consider upgrading to Premium for more benefits!"
# If the user has a medical condition and chooses Premium, print: "We recommend a free consultation before starting."


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
  
membership_type = input("Choose a membership type (basic or premium). ").lower() 
 
if (membership_type == "basic"):
  personal_training = input("Do you want personal training (yes or no)? ")
  if (personal_training == 'yes'):
    print("Basic plan with personal training: $45 per month.")
  elif (personal_training == 'no'):
    print("Basic plan: $30 per month.")
    print("Consider upgrading to Premium for more benefits!")
  else:
    print("Invalid input. Please enter 'yes' or 'no'.")
elif (membership_type == "premium"):
  print("Premium plan: $60 per month.")
  if (age < 30):
    print("You qualify for a youth discount! 10% off your plan.")
  if (medical_condition == "yes"):
    print("We recommend a free consultation before starting.")

else:
  print("Invalid input. Please enter 'basic' or 'premium'.")
  
