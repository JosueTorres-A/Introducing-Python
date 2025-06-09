# 2.1 How many seconds are in an hour? Use the interactive interpreter as a calculator
# and multiply the number of seconds in a minute (60) by the number of minutes in an
# hour (also 60).
minutes_per_hour = 60
seconds_per_minute = 60

print(minutes_per_hour * seconds_per_minute)

# 2.2 Assign the result from the previous task (seconds in an hour) to a variable called
# seconds_per_hour.
seconds_per_hour = minutes_per_hour * seconds_per_minute

print("There are", seconds_per_hour, "seconds in an hour.")

# 2.3 How many seconds are in a day? Use your seconds_per_hour variable.
hours_per_day = 24

print(hours_per_day * seconds_per_hour)

# 2.4 Calculate seconds per day again, but this time save the result in a variable called
# seconds_per_day.
seconds_per_day = hours_per_day * seconds_per_hour

print("There are", seconds_per_day, "seconds in a day.")

# 2.5 Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.
result_float = seconds_per_day / seconds_per_hour

print(result_float)

# 2.6 Divide seconds_per_day by seconds_per_hour, using integer (//) division. Did
# this number agree with the floating-point value from the previous question, aside
# from the final .0?
result_integer = seconds_per_day // seconds_per_hour

print(result_integer)