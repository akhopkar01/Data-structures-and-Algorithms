## Maps and Hash

# Caching
# Solve the recursive staircase problem using caching
# General Solution with recursion -> output = staircase(n-1) + staircase(n-2) + staircase(n-3)

def staircase(n):
    num_map = dict()
    return _staircase_fast(n, num_map)

def _staircase_fast(n, num_map):
    if n == 1:
        output = 1
    elif n == 2:
        output = 2
    elif n == 3:
        output = 4

    else:
        if (n-1) in num_map:
            firsts = num_map[n-1]
        else:
            firsts = _staircase_fast(n-1, num_map)

        if (n-2) in num_map:
            seconds = num_map[n-2]
        else:
            seconds = _staircase_fast(n-2, num_map)

        if (n-3) in num_map:
            thirds = num_map[n-3]
        else:
            thirds = _staircase_fast(n-3, num_map)
        output = firsts + seconds + thirds
    num_map[n] = output
    return output


def pair_sum(input_list, target):
    nmap = dict()
    for i, num in enumerate(input_list):
        if (target - num) in nmap:
            return [nmap[target - num], i]
        nmap[num] = i
    return [-1, -1]


def longest_consecutive_subsequence(input_list):
    dict_map = dict()
    for i, num in enumerate(input_list):
        dict_map[num] = i

    max_length = -1

    start = -1
    for i, num in enumerate(input_list):
        current_start = i
        dict_map[num] = -1
        current_count = 1

        current = num + 1
        while current in dict_map and dict_map[current] > 0:
            dict_map[current] = -1
            current_count += 1
            current += 1

        current = num - 1
        while current in dict_map and dict_map[current] > 0:
            current_start = dict_map[current]
            dict_map[current] = -1
            current_count += 1
            current -= 1

        if current_count >= max_length:
            if current_count == max_length and current_start > start:
                continue
            start = current_start
            max_length = current_count

    start_num = input_list[start]

    return [num for num in range(start_num, start_num + max_length)]

if __name__ == "__main__":
    test = [4, 5, 6]
    print(staircase(4), staircase(5), staircase(6))
    t2 = [2, 4, 6, 1, 9]
    print(pair_sum(t2, 13))