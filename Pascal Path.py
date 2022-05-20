import math
total_test_case = int(input())

def sum_of_power(n):
    lst = []
    stack = 1
    while (n > 0):
        if (n % 2 == 1):
            lst.append(stack)
            n -= 1
        else:
            stack *= 2
            n = n/2
    return lst

def solution(n):
    path = []
    if (n <= 30):
        for i in range (1, n + 1):
            path.append([i, 1])
    else:
        sum_of_2 = sum_of_power(n-30)
        l = len(sum_of_2)
        conti = 1
        first = 1
        for i in range(0, l):
            line = int(math.log2(sum_of_2[i])) + 1
            for j in range(conti, line + 1):
                if (j == line):
                    if (first == 1):
                        for k in range(1, line + 1):
                            path.append([j, k])
                        first = 0
                    elif (first == 0):
                        for k in range(0, line):
                            path.append([j, j - k])
                        first = 1
                elif (j < line):
                    if first == 1:
                        path.append([j,first])
                    elif (first == 0):
                        path.append([j,j])
            conti = line + 1
        missing_one = 30 - int(math.log2(sum_of_2[i])) + l -1
        for i in range(0, missing_one):
            if first == 1:
                path.append([conti + i, first])
            elif (first == 0):
                path.append([conti + i, conti + i])
    return path

for no_test in range(1, total_test_case + 1):
    print("Case #%d:" %no_test)
    result = solution(int(input()))
    for i in range (0, len(result)):
        step = result[i]
        print(*step)