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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


class comm_logs:
    def __init__(self, log):
        self.logs = log

    def get_records_(self):
        if len(self.logs[0]) == 3:
            print("First record of texts, {} texts {} at time {} ".
                  format(self.logs[0][0], self.logs[0][1], self.logs[0][2]))
        if len(self.logs[0]) == 4:
            print("Last record of calls, {} calls {} at time {}, lasting {} seconds".
                  format(self.logs[-1][0], self.logs[-1][1], self.logs[-1][2], self.logs[-1][3]))

log_files = [texts, calls]
for items in log_files:
    logs = comm_logs(items)
    logs.get_records_()