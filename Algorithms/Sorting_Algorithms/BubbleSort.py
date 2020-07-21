# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24, 13), (21, 55), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3)]

def get_hours(time):
    h, m = time
    return 100 * h + m

def bubble_sort_2(l):
    # TODO: Implement bubble sort solution
    for i in range(len(l)):
        for j in range(1, len(l)):
            this = l[j]
            prev = l[j - 1]
            if get_hours(prev) >= get_hours(this):
                continue

            l[j - 1] = this
            l[j] = prev

    return l

    pass


print(bubble_sort_2(sleep_times))
print("Pass" if (sleep_times == [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)]) else "Fail")