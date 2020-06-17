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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def unique_codes(log):
    numbers = set()
    for caller, callee, _, _ in log:
         # numbers.add(caller)
         numbers.add(callee)
    numbers_call_log = list(numbers)
    codes = set()
    for number in numbers_call_log:
        fixed_line_number = number.split(")")
        if len(fixed_line_number) == 2:
            code, usr_number = fixed_line_number
            code = code.split("(")[1]
        elif fixed_line_number[0][0] == '7' or fixed_line_number[0][0] == '8' or fixed_line_number[0][0] == '9':
            code = fixed_line_number[0][:4]
        elif fixed_line_number[0][:3] == '140':
            code = '140'
        codes.add(code)
    return list(codes)


def get_line_code(number):
    fixed_line_number = number.split(")")
    if len(fixed_line_number) == 2:
        code, usr_number = fixed_line_number
        code = code.split("(")[1]
        return code
    else:
        return None

def fixed_line_percentage(log):
    total = 0
    correct = 0
    for caller, callee, _, _ in log:
        caller_code = get_line_code(caller)
        callee_code = get_line_code(callee)
        if caller_code is not None and caller_code == '080':
            total+=1
            if callee_code is not None and callee_code =='080':
                correct+=1
    percentage = round((correct/total)*100, 2)
    return percentage

if __name__ == "__main__":
    print("################## 3A ###################")
    codes = unique_codes(calls)
    print("The numbers called by people in Bangalore have codes: \n{}".format('\n'.join(codes)))

    print("################## 3B ####################")
    percentage = fixed_line_percentage(calls)
    print("%s percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."%percentage)
