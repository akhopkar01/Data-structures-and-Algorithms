import time

def daysBetweenDates1(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """

    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though!
    # Maintain a calender as dictionary.
    months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if 0 < month1 <= 12 and 0 < month2 <= 12:
        if year1 < year2:
            if month1 == month2:
                if day1 <= day2:
                    days = 365 * (year2 - year1) + (day2 - day1)
                # day_offset = 0
                if day2 < day1:
                    days = 365 * (year2 - year1) - (day1 - day2)
                return days
            if month1 != month2:
                days = months[month1] - day1
                month1 += 1
                while year1 < year2:
                    while month1 <= 12:
                        days += months[month1]
                        month1 += 1
                    if isLeapYear(year1):
                        days += 1
                    month1 = 1
                    year1 += 1
                while month1 < month2:
                    days += months[month1]
                    month1 += 1
                days += day2

        elif year1 == year2:
            if month1 < month2:
                days = months[month1] - day1
                month1 += 1
                while month1 < month2:
                    days += months[month1]
                    month1 += 1
                days += day2
            elif month1 == month2 and day1 <= day2:
                days = day2 - day1
            else:
                return 0
        else:
            return 0
    return days


def isLeapYear(year):
    return year % 4 == 0


def daysInMonth(month, year):
    months = {
        1: 31,
        2: 28 if not isLeapYear(year) else 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    return months[month]


def nextDay(year, month, day):
    if month == 12 and day >= daysInMonth(month, year):
        day = 1
        year += 1
        month = 1
    elif day >= daysInMonth(month, year):
        day = 1
        month += 1
    else:
        day += 1
    return year, month, day


def checkDates(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    elif year1 == year2:
        if month1 < month2:
            return True
        elif month1 == month2 and day1 < day2:
            return True
        return False
    return False


def daysBetweenDates2(year1, month1, day1, year2, month2, day2):
    days = 0
    while checkDates(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        # print(year1, month1, day1)
        days += 1
    return days


if __name__ == "__main__":
    testcases = {
        "test1": {
            "date1": [30, 12, 2017],
            "date2": [31, 12, 2017]
        },
        "test2": {
            "date1": [30, 12, 2017],
            "date2": [1, 1, 2018]
        },
        "test3": {
            "date1": [30, 12, 2017],
            "date2": [31, 12, 2017]
        },
        "test4": {
            "date1": [29, 6, 2012],
            "date2": [1, 6, 2013]
        },
        "test5": {
            "date1": [30, 12, 2017],
            "date2": [28, 12, 2017]
        },
        "test6": {
            "date1": [1, 4, 1994],
            "date2": [1, 10, 1997]
        },
        "test7": {
            "date1": [1, 1, 1900],
            "date2": [31, 12, 1999]
        }
    }
    methods = ["Method 1", "Method 2"]
    for method in methods:
        print("-------{}------".format(method))
        t0 = time.time()
        for test in testcases:
            date1, date2 = testcases[test]["date1"], testcases[test]["date2"]
            year1, month1, day1 = date1[::-1]
            year2, month2, day2 = date2[::-1]

            if method == "Method 1":
                print("Days between {} & {} : {} ".format(date1, date2, daysBetweenDates1(year1, month1, day1,
                                                                                          year2, month2, day2)))
            if method == "Method 2":
                print("Days between {} & {} : {} ".format(date1, date2, daysBetweenDates2(year1, month1, day1,
                                                                                          year2, month2, day2)))
        t1 = time.time()
        print("Completed all testcases for {} in {} ".format(method, t1-t0))