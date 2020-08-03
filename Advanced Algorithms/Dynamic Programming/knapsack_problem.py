import collections
import time

Item = collections.namedtuple('Item', ['weight', 'value'])

"""
The Naive Approach - Based on Recursion:
The idea is, for each given item, if the item-weight is less than the remaining capacity (kg) of the knapsack, then calculate the value ( $ ) of the knapsack if we:

Do not put the item in the knapsack - Value ( $ ) of the knapsack will be the output of the knapsack_recursive() function, 
with the same remaining capacity, and check for the next item down the list.
Put the item in the knapsack - Value ( $ ) of the knapsack will be the sum of the current value of the item and output of the knapsack_recursive() function, 
with updated remaining capacity, and check for the next item down the list.
Return the maximum of either of the above two values. In knapsack_recursive() function, begin with developing the solution for the base case i.e., smallest subproblem.

Note - Below is the implementation of this naive approach with recursion, that has an exponential time complexity as  𝑂(2𝑛) , 
where  𝑛  is the number of given items, becuase we are evaluating both the two options (put/not put) for each given item.
"""

def knapsack_max_value_sol1(knapsack_max_weight, items):
    last = len(items) -1
    return knapsack_recursive(knapsack_max_weight, items, last)

def knapsack_recursive(capacity, items, last):
    if capacity <= 0 or last < 0:
        return 0

    valueA = 0
    if items[last].weight <= capacity:
        valueA = items[last].value + knapsack_recursive(capacity - items[last].weight, items, last-1)

    valueB = knapsack_recursive(capacity, items, last-1)

    return max(valueA, valueB)

"""
The Approach - Dynamic Programming
Store and reuse the intermediate results in a lookup table. This step is called memoization. 
Start with initializing a lookup table (a list), where the index represents the remaining capacity (kg) of the knapsack, 
and the element represents the maximum value ( $ ) that it can hold.

For a given item, if the item-weight is less than the remaining capacity (kg) of the knapsack, then we have two options:

Do not pick the item - In this case, the value ( $ ) of knapsack with the remaining capacity would not change. It can be represented as lookup_table[capacity].
Pick the item - In this case, the value ( $ ) and capacity (kg) of the knapsack would be updated. 
The value ( $ ) of the knapsack will be equal to value ( $ ) of the current object + value ( $ ) in the lookup table at [capacity - item.weight] position. 
It can be represented as lookup_table[capacity - item.weight] + item.value.
Update the lookup table, lookup_table[capacity], with the maximum of either of the above two values.

Note - This approach with dynamic programming will have a time complexity as  𝑂(2𝑛𝐶)≡𝑂(𝑛𝐶) , 
where  𝑛  is the number of given items and  𝐶  is the max capacity (kg) of the knapsack.
"""

def knapsack_max_value_sol2(knapsack_max_weight, items):

    lookup = [0 for _ in range(knapsack_max_weight + 1)]

    for item in items:

        for capacity in range(knapsack_max_weight, 0, -1):

            if item.weight <= capacity:
                valueA = item.value + lookup[capacity - item.weight]
                valueB = lookup[capacity]
                lookup[capacity] = max(valueA, valueB)

    return lookup[-1]

tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]

start_time = time.time()
for test in tests:
    assert test['correct_output'] == knapsack_max_value_sol1(**test['input'])
print("Time Taken by solution 1: ", time.time() - start_time)

start_time = time.time()
for test in tests:
    assert test['correct_output'] == knapsack_max_value_sol2(**test['input'])
print("Time Taken by solution 2: ", time.time() - start_time)

