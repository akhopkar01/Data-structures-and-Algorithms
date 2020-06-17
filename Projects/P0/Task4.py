"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

caller_directory={}
text_directory={}

for caller, callee, _, _ in calls:
    caller_directory[caller] = callee
for texter, textee, _ in texts:
    text_directory[texter] = textee

maybe_telemarketer=set()
for key in caller_directory:
    if key not in caller_directory.values():
        if key not in text_directory.keys() and key not in text_directory.values():
            maybe_telemarketer.add(key)


print("These numbers could be telemarketers: \n{}".format('\n'.join(maybe_telemarketer)))
