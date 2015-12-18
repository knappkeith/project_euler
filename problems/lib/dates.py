week_days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"]

def get_month_array(month, year):
    pass


def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    if year % 4 == 0:
        return True
    return False


def february_days(year):
    if is_leap_year(year):
        return 29
    else:
        return 28


def days_in_month(month, year):
    if isinstance(month, str):
        month = convert_month_str_to_int(month)
    days = [
        31,
        february_days(year),
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31]
    return days[month - 1]


def convert_month_str_to_int(month):
    if month.upper() == "JAN" or month.upper() == "JANUARY":
        return 1
    elif month.upper() == "FEB" or month.upper() == "FEBRUARY":
        return 2
    elif month.upper() == "MAR" or month.upper() == "MARCH":
        return 3
    elif month.upper() == "APR" or month.upper() == "APRIL":
        return 4
    elif month.upper() == "MAY":
        return 5
    elif month.upper() == "JUN" or month.upper() == "JUNE":
        return 6
    elif month.upper() == "JUL" or month.upper() == "JULY":
        return 7
    elif month.upper() == "AUG" or month.upper() == "AUGUST":
        return 8
    elif month.upper() == "SEP" or month.upper() == "SEPTEMBER":
        return 9
    elif month.upper() == "OCT" or month.upper() == "OCTOBER":
        return 10
    elif month.upper() == "NOV" or month.upper() == "NOVEMBER":
        return 11
    elif month.upper() == "DEC" or month.upper() == "DECEMBER":
        return 12
    else:
        raise ValueError("Unknown Month: %s" % month)