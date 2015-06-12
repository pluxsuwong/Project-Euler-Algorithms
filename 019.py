# Problem 19 - Counting Sundays
print "Problem 19 - Counting Sundays"

# day, date, month, year
'''
INCLUSIVE!
day: 1 - 7
date: 1 - 30 | 1 - 31 | 1 - 28
month: 1 - 12
year: 1900 - 2000 (but remove Sundays in 1900)
'''
index = {"CTR":0, "DAY":1, "DATE":1, "MONTH":1}

def sundays_in_yr(year):
    global index
    days = 0
    day_ctr = 0
    is_leap_year = False
    is_new_month = False
    is_new_year = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap_year = True
                # print("*"),
        else:
            is_leap_year = True

    # if is_leap_year:
        # print("LY - "),

    while not is_new_year:
        # Increment counter
        if index["DAY"] % 7 == 0 and index["DATE"] == 1:
            index["CTR"] += 1
        
        # Cycle through days
        if index["DAY"] == 7:
            index["DAY"] = 1
        else:
            index["DAY"] += 1

        # Cycle through dates
        if index["DATE"] < 28:
            index["DATE"] += 1
        else:
            last_date = 0
            if index["MONTH"] <= 7:
                if index["MONTH"] % 2 == 0:
                    if index["MONTH"] == 2:
                        if is_leap_year:
                            last_date = 29
                        else:
                            last_date = 28
                    else:
                        last_date = 30
                else:
                    last_date = 31
            else:
                if index["MONTH"] % 2 == 0:
                    last_date = 31
                else:
                    last_date = 30
            if index["DATE"] == last_date:
                index["DATE"] = 1
                is_new_month = True
            else:
                index["DATE"] += 1

        # Cycle through months
        if is_new_month:
            if index["MONTH"] == 12:
                index["MONTH"] = 1
                is_new_year = True
            else:
                index["MONTH"] += 1
            is_new_month = False
    return None

surplus = 0
for year in range(1900, 2001):
    sundays_in_yr(year)
    if year == 1900:
        index["CTR"] = 0
    # print "Year: ", str(year), str(index["CTR"])

print "Final tally: ", str(index["CTR"])
