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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def unique_numbers(log):
    numbers = set()
    for entries in log:
         # print(entries[:2])
         caller, callee = entries[0:2]
         numbers.add(caller)
         numbers.add(callee)
    return numbers

logs ={"texts":texts,
       "calls":calls}

for log in logs:
    print("There are %s different telephone numbers in the %s records. "%(len(unique_numbers(logs[log])), log))