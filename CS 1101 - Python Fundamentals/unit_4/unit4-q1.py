# Currently, the code includes several repeated sections, such as calculating weekly averages, determining if daily goals were met, and displaying a performance summary. This repetition makes the program long and difficult to maintain. Your task is to simplify and improve the program by creating custom functions that perform these repeated tasks more efficiently. You must also decide how to handle variable scope so that weekly totals and progress data are shared properly between functions without overwriting or duplicating information.


# Explain how you would design one or more custom functions to make this fitness tracker more reusable and organized. Provide a code demonstrating what arguments your function(s) would take, and what values they would return.

# calculating weekly averages


# first define a variable to stores the total steps taken
# then the total step would be divided by the either the default value in the parameter or the argument received.

# the average is then printed

total_steps = 21000
progress_data = 3000

# A simple question for you: how would daily_progress() need to change if you wanted it to also account for a small tolerance range, like being within 100 steps of the goal?


def weekly_average(total_steps, days=7):
    return round(total_steps / days, 2)


def daily_progress(daily_steps, goal):
    if daily_steps == goal:
        return "Congratulations! You've met your step goal for today."
    elif daily_steps > goal:
        return "Congratulations! You've exceeded your step goal for today."
    elif daily_steps >= (goal - 100):
        return "You did great today. You were almost at your goal."
    else:
        return "Daily goal not reached."

# performance summary
def performance_summary(avg, goal):
    difference = round(avg - goal, 2)
    if avg >= goal:
      print(difference)
      return f"Weekly average: {avg} steps. You averaged {difference} steps above your daily goal of {goal}."
    else:
      return f"Weekly average: {avg} steps. You fell short of your daily goal of {goal} by {abs(difference)} steps."


total_steps = 21000
goal = 2000

avg = weekly_average(total_steps)
print(avg)
print(daily_progress(2000, goal))
print(performance_summary(avg, goal))

def daily_progress(daily_steps, goal):
    if daily_steps == goal:
        return "Congratulations! You've met your step goal for today."
    elif daily_steps > goal:
        return "Congratulations! You've exceeded your step goal for today."
    else:
        return "Daily goal not reached."

weekly_steps = [8000, 11000, 7500, 9200, 6800, 10500, 9900]
goal = 9000

for day, steps in enumerate(weekly_steps, start=1):
    print(f"Day {day}: {daily_progress(steps, goal)}")
    
def create_summary(averages, goals_met):
    return f"Average steps: {averages['avg_steps']:.0f}, " \
           f"Average calories: {averages['avg_calories']:.0f}, " \
           f"Average minutes: {averages['avg_minutes']:.0f}. " \
           f"Goals met today: {goals_met}"
           
