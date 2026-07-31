# Question 1: Create a Python program that manages a list of books available in the library by performing operations such as creating, adding, removing, and displaying book titles.
# Create a list of book titles: ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"].
# Add two more books to the list using append().
# Remove one book that has been damaged using remove().
# Sort the list alphabetically and display the final list using sort().

book_titles = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]

# Add books to book_titles
book_titles.append("The Great Gatsby")
book_titles.append("To Kill a Mockingbird")
print(book_titles)

# remove books from book_titles
book_titles.remove("To Kill a Mockingbird")
print(book_titles)

# Sort list alphabetically
book_titles.sort()
print(book_titles)