# Question 4: Use indexing and slicing to manage weekly borrowing statistics.
# Given a list borrowed_books = [23, 19, 31, 27, 22, 30, 25] representing the number of books borrowed each week, extract the records from week 2 to week 5 using slicing.
# Replace the number of books borrowed in week 1 with 20 using indexing.
# Display the updated list and the sliced portion.


borrowed_books = [23, 19, 31, 27, 22, 30, 25]
# slicing week 2 to week 5
week2_to_5 = borrowed_books[1:5]

# updating values using indexing
borrowed_books[0] = 20
print(borrowed_books)
print(week2_to_5)



x = [2, 3, 4, 5]
print(x[4])