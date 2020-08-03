"""
In text analysis, it is often useful to compare the similarity of two texts
(imagine if you were trying to determine plagiarism between a source and answer text).
In this notebook, we'll explore one measure of text similarity, the Longest Common Subsequence (LCS).

The Longest Common Subsequence is the longest sequence of letters that are present in both the given two strings in the same relative order.

Example - Consider the two input strings, str1 = 'ABCD' and str2 = 'AXBXDX'.
The LCS will be 'ABD' with the length as 3 letters. It is because each of the letters 'A' , 'B', and 'D' are present in both the given two strings
in the same relative order.

Note that:

An LCS need not necessarily be a contiguous substring.
There can be more than one LCS present in the given two strings.
There can be many more common subsequences present here, with smaller length. But, in this problem we are concerned with the longest common subsequence.
"""

def lcs(string1, string2):

    lookup = [[0 for _ in range(len(string2)+1)] for _ in range(len(string1)+1)]

    for i, char_a in enumerate(string1):
        for j, char_b in enumerate(string2):
            if char_a == char_b:
                lookup[i+1][j+1] = lookup[i][j] + 1
            else:
                top_element = lookup[i][j+1]
                left_element = lookup[i+1][j]
                lookup[i+1][j+1] = max(top_element, left_element)
    return lookup[-1][-1]

# Run this cell to see how your function is working
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1==5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2==7, "Incorrect LCS value."
print('Tests passed!')