# from datetime import datetime, timedelta

# # First date and time
# first_datetime = datetime.strptime('2024-02-19 10:00:00', '%Y-%m-%d %H:%M:%S')

# # Current date and time
# current_datetime = datetime.now()

# # Extract date and time components
# first_date = first_datetime.date()
# first_time = first_datetime.time()

# current_date = current_datetime.date()
# current_time = current_datetime.time()

# # Calculate the difference between dates
# date_difference = current_date - first_date

# # Calculate the difference between times
# time_difference = datetime.combine(datetime.min, current_time) - datetime.combine(datetime.min, first_time)

# # Total difference in days, hours, and minutes
# total_days = date_difference.days
# total_hours = time_difference.total_seconds() // 3600
# total_minutes = (time_difference.total_seconds() % 3600) // 60

# print("Total Difference:")
# print("Days:", total_days)
# print("Hours:", total_hours)
# print("Minutes:", total_minutes)

from datetime import datetime, timedelta

# First date and time
first_datetime = datetime.strptime('2024-02-19 10:00', '%Y-%m-%d %H:%M')

# Current date and time
current_datetime = datetime.now()

# Extract date and time components
first_date = first_datetime.date()
first_time = first_datetime.time()

current_date = current_datetime.date()
current_time = current_datetime.time()

# Calculate the difference between dates
date_difference = current_date - first_date

# Calculate the difference between times
time_difference = datetime.combine(datetime.min, current_time) - datetime.combine(datetime.min, first_time)

# Total difference in days, hours, and minutes
total_hours = time_difference.total_seconds() / 3600

# Charge rate
charge_rate_per_hour = 10  # in rupees

# Total cost
total_cost = total_hours * charge_rate_per_hour

print("Total Difference in Hours:", total_hours)
print("Total Cost: {} rupees".format(total_cost))

