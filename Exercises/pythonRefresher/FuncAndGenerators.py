def prod(a,b):
    # TODO change output to the product of a and b
    output = a * b
    return output

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        n, i = output, i+1


def check_sudoku(matrix):
    # We define a map to verify matrix entries
    map = [i for i in range(1, len(matrix)+1)]

    # Check Row
    for i in range(len(matrix)):
        nodes = []
        for j in range(len(matrix)):
            if matrix[i][j] in map:
                if matrix[i][j] in nodes:
                    return False
                nodes.append(matrix[i][j])
            else:
                return False

    # Check Column
    for j in range(len(matrix)):
        nodes = []
        for i in range(len(matrix)):
            if matrix[i][j] in map:
                if matrix[i][j] in nodes:
                    return False
                nodes.append(matrix[i][j])
            else:
                return False
    return True


if __name__ == "__main__":
    choice = int(input("Program 1 or Program 2 [numeric entry] "))
    if choice == 1:
        factorial = fact_gen()
        num = int(input("Factorials upto which number "))
        for i in range(num):
            print(next(factorial))

    if choice == 2:
        testcases =  dict(test1 = [[1, 2, 3],
                   [2, 3, 1],
                   [3, 1, 2]], # Correct
        test2 = [[1, 2, 3, 4],
                     [2, 3, 1, 3],
                     [3, 1, 2, 3],
                     [4, 4, 4, 4]], # Incorrect
        test3 = [[1, 2, 3, 4],
                      [2, 3, 1, 4],
                      [4, 1, 2, 3],
                      [3, 4, 1, 2]], #Incorrect

        test4 = [[1, 2, 3, 4, 5],
                      [2, 3, 1, 5, 6],
                      [4, 5, 2, 1, 3],
                      [3, 4, 5, 2, 1],
                      [5, 6, 4, 3, 2]], # Incorrect

        test5 = [['a', 'b', 'c'],
                      ['b', 'c', 'a'],
                      ['c', 'a', 'b']], #Incorrect

        test6 = [[1, 1.5],
                      [1.5, 1]] #Incorrect
                          )
        for test in testcases:
            print("Output for {} : {}".format(test, check_sudoku(testcases[test])))