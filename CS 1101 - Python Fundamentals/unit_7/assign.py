import os
# Question 1:
# You are assisting a university event coordinator who has collected feedback messages from students after a guest lecture. Many of the comments are messy and inconsistently formatted, and your task is to clean the text before saving it in a report.
# One of the raw feedback is: “ THE SPEAKER WAS GREAT but THE ROOM WAS COLD ”
# Manipulate the string above by removing any leading and trailing spaces using strip() and converting all letters to lowercase with lower().

raw_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "
stripped_feedback = raw_feedback.strip()
print(stripped_feedback)

lowercased_feedback = stripped_feedback.lower()
print(lowercased_feedback)

# Manipulate the wording to standardize it by replacing "speaker" with "presenter" using replace(), then remove any extra internal spaces with " ".join(s.split()).
# Manipulate the cleaned text into title case using title() and display the final output using an f-string.

standardized = lowercased_feedback.replace('speaker', 'presenter')
print(standardized)

joined = " ".join(standardized.split())
print(joined)

titled = joined.title()
print(f'Final cleaned output: {titled}')

# Question 2:
# The event coordinator now wants to save and view the cleaned feedback created earlier. You will use Python’s file-handling features to write, read, and update the feedback stored in a text file.
# Implement file writing by creating a list called feedback_list that contains three cleaned feedback messages. Write them to a text file named feedback.txt, each on a new line.
# Implement file reading by opening feedback.txt and printing all feedback lines one by one.
# Implement file appending by adding one more feedback message to the same file, then read and print the full updated list again.

feedback_list = [
    'The guest lecture was very insightful!!',
    'Great speaker, but the room was too crowded...',
    'I learned a lot, thank you for organizing this event.'
]

# File writing
if not os.path.exists("feedback.txt"):
  with open("feedback.txt", "w") as write_feedback:
    for feedback in feedback_list:
      write_feedback.write(feedback + "\n")
else:
  print("The file you wish to create already exists")
    
    
# file reading
try:
  with open("feedback.txt") as read_feedback:
      print("Feedback list: ")
      for feedback in feedback_list:
        print(read_feedback.read())
except:
  print("The file you wish to read does not exist")
 

# File appending
try:
  with open("feedback.txt", "a") as append_feedback:
        append_feedback.write("The Q&A session at the end was really helpful.")
        if not os.path.exists("feedback.txt"):
          with open("feedback.txt", "w") as write_feedback:
            for feedback in feedback_list:
              write_feedback.write(feedback + "\n")
        else:
          print("The file you wish to create already exists")
except:
  print("The file does not exist")   

# Question 3:
# The event coordinator sometimes may try to open the feedback.txt file before it exists or while it is being used by another program. To prevent the program from crashing, you need to add exception handling that manages these file errors safely.
# Apply exception handling by placing your code for reading feedback.txt inside a try and except block.
# Apply specific error handling by printing:
# "File not found. Please create feedback.txt first." for FileNotFoundError
# "Permission denied. Close the file and try again." for PermissionError
# Apply a finally block to always print "Operation completed." whether the file is opened successfully or not.



# Question 4:
# The event coordinator wants to know how many students used the word “great” in their feedback. Using Python, you will analyze the contents of the feedback file, count mentions of this word, and create a short summary report.
# Implement a file-reading step that opens feedback.txt and reads all lines. Use lower() and find() (or the in operator) to count how many feedback entries contain the word “great” (case-insensitive).
# Implement a file-writing step that creates a new file named summary.txt and writes the following lines into it:
# === Workshop Feedback Summary ===
# Total Feedback: X
# Mentions of 'Great': Y
# Implement a formatted print statement that displays the same summary neatly on the console using f-strings.
