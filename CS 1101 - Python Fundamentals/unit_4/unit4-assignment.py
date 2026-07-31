
# cups_sold = 200

# def update_sales():
#   print("Global variable -", cups_sold)
#   cups_sold = 250
#   print("Local variable -", cups_sold)
  

# update_sales()

# The  the function update_sales(), which is the local variable would take precedence over the varaible outside the function when the function is called.



days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
daily_orders = [120, 150, 180, 90, 200]

daily_revenue = list(map(lambda order: order * 5, daily_orders))
highest_daily_sales = max(daily_orders)
busiest_day = max(days, key=lambda day: daily_orders[days.index(day)])

print("Daily revenue:", daily_revenue)
print("Highest daily sales value:", highest_daily_sales)
print("Busiest day:", busiest_day)

