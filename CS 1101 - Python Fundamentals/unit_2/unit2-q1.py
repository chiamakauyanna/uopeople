# Write a Python program for SmartFit that asks the user to enter their age.
# If the age is below 18, print: "You are eligible for the Teen Fitness Program."
# If the age is between 18 and 40, print: "You are eligible for the Regular Fitness Program."
# Otherwise, print: "You are eligible for the Senior Wellness Program."


age = int(input("How old are you? "))

if (age < 18):
  print("You are eligible for the Teen Fitness Program.")
elif(age >= 18 and age < 40):
  print("You are eligible for the Regular Fitness Program.")
else:
  print("You are eligible for the Senior Wellness Program.")