# Question 3: Perform tuple packing and unpacking in a Python program to demonstrate how book information can be stored and accessed efficiently.
# Pack a book title, author, and publication year into a tuple called book_info.
# Unpack the tuple into separate variables and print them in a readable format (for example: “Title: The Alchemist”).
# Explain how tuple packing and unpacking make code more organized and easier to understand.

# packing a tuple
book_info = ("To Kill a Mockingbird", "Harper Lee", 1960)

# unpacking the book_info tuple
title, author, publication_year = book_info

print("Title:", title)
print("Author:", author)
print("Publication year:",publication_year)
