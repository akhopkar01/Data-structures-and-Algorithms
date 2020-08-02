"""
Given arrival and departure times of trains on a single day in a railway platform, find out the minimum number of platforms required so that no train has to wait for the other(s) to leave. In other words, when a train is about to arrive, at least one platform must be available to accommodate it.

You will be given arrival and departure times both in the form of a list. The size of both the lists will be equal, with each common index representing the same train. Note: Time hh:mm would be written as integer hhmm for e.g. 9:30 would be written as 930. Similarly, 13:45 would be given as 1345

Example:
Input: A schedule of 6 trains:

arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
Expected output: Minimum number of platforms required = 3
"""


def min_platforms(arrival, departure):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    so that no train has to wait for other(s) to leave
    """
    arrival.sort()
    departure.sort()

    platforms_required = 1
    max_platform_required = 1

    i = 1
    j = 0

    while i < len(arrival) and j < len(departure):
        if arrival[i] < departure[j]:
            platforms_required += 1
            i += 1

            if platforms_required > max_platform_required:
                max_platform_required = platforms_required

        else:
            platforms_required -= 1
            j += 1

    return max_platform_required


def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]

    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)

