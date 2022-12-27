# Get input from the user
date = int(input("Enter the date (1-31  "))
month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year (e.g. 2003): "))

# Convert the month number to the month name
month_name = ""
if month == 1:
    month_name = "Jan"
elif month == 2:
    month_name = "Feb"
elif month == 3:
    month_name = "Mar"
elif month == 4:
    month_name = "Apr"
elif month == 5:
    month_name = "May"
elif month == 6:
    month_name = "Jun"
elif month == 7:
    month_name = "Jul"
elif month == 8:
    month_name = "Aug"
elif month == 9:
    month_name = "Sep"
elif month == 10:
    month_name = "Oct"
elif month == 11:
    month_name = "Nov"
elif month == 12:
    month_name = "Dec"

# Add "st", "nd", "rd", or "th" to the date
date_suffix = ""
if date % 10 == 1 and date != 11:
    date_suffix = "st"
elif date % 10 == 2 and date != 12:
    date_suffix = "nd"
elif date % 10 == 3 and date != 13:
    date_suffix = "rd"
else:
    date_suffix = "th"

# Output the result
print(f"{date}{date_suffix} {month_name}. {year}")
