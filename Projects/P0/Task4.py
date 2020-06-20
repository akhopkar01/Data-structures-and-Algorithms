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

callers = set()
callees = set()
texters = set()
textees = set()

for caller, callee, _, _ in calls:
    callers.add(caller)
    callees.add(callee)

for texter, textee, _ in texts:
    texters.add(texter)
    textees.add(textee)


telemarketers = callers - callees - texters - textees

potential_telemarketers = sorted(telemarketers)
print("These numbers could be telemarketers: \n{}".format('\n'.join(potential_telemarketers)))
