import datetime as dt



months = [ ["January", 31], ["February", 28], ["March", 31], ["April", 30], ["May", 31], ["June", 30], ["July", 31], ["August", 31], ["September", 30], ["October", 31], ["November", 30], ["December", 31]   ]
year = 1901
month = 1
day = 1
sundays_count = 0
month_counter = 0

# 1 Jan 1901 = Tuesday, 1 = Tuesday
print(dt.datetime(1901, 1, 1).weekday())



while True:
    
    # Find the current date
    today = dt.datetime(year, month, day) # Year, Month, Day

    # Check if the day is a "Sunday", and if its the first day of the month
    if today.weekday() == 6 and day == 1: 
        # Increment the amount of soundays
        sundays_count += 1

    # If the year is the final date
    if year == 2000 and month == 12 and day == 31:
        # Exit the loop
        break

    # If the day isn't at the end of the month yet
    if day != months[month_counter][1]:
        day += 1

    # If it is
    else:
        # If the month is December:
        if month_counter == 11:
            # Go to the next year
            year += 1
            # Reset the month
            month_counter = 0
            month = 1
            # Reset the day we are in the month
            day = 1

            # Check if the year is a leap year
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                # Set February to have only 29 days
                months[1][1] = 29

            # If it isn't a leap year
            else:
                # Set February to have only 28 days
                months[1][1] = 28

        # If the month isn't December
        else:
            # Go to the next month
            month_counter += 1
            month += 1
            # Reset the day we are in the month
            day = 1

    #print(today)

print(year, month, day)
print("Sundays count", sundays_count)
