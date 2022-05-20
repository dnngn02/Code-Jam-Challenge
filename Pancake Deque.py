import copy
total_test_case = int(input())

def solution():
    number = int(input())
    deque = list(map(int, input().split()))
    pay = 0
    max = 0
    for i in range(number):
        if deque[0] < deque[-1]:
            less = deque[0]
            first = 0
        else:
            less = deque[-1]
            first = -1
        if max == 0:
            pay += 1
            max = less
        else:
            if less >= max:
                pay += 1
                max = less
        deque.pop(first)
    return pay

for no_test in range(1, total_test_case + 1):
    print("Case #%d: %s" % (no_test, solution()))