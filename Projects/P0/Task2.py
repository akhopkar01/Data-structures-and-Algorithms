"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call_records = {}
for caller, callee, time, duration in calls:
    call_records[caller] = 0
    call_records[callee] = 0

for caller, callee, time, duration in calls:
    call_records[caller] += int(duration)
    call_records[callee] += int(duration)

max_phone_number = max(call_records, key=call_records.get)

print("{} spent the longest time, {} seconds, on the phone during September 2016 ".format(max_phone_number, call_records[max_phone_number]))


