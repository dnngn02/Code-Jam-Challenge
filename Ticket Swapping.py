total_test_case = int(input())

def cost(N, diff):
    return diff * (N + N - diff + 1) /2

def solution():
    N, M = map(int, input().split())
    enter = []
    leave = []
    original_cost = 0
    for i in range(M):
        s = (list(map(int, input().split())))
        start = s[0]
        end = s[1]
        no = s[2]
        for j in range(no):
            enter.append(start)
            leave.append(end)
        original_cost += (cost(N, end - start) * no)
    min_cost = 0
    available_tickets = []
    for i in range(N + 1):
        if i in enter:
            count = enter.count(i)
            for j in range(count):
                available_tickets.append(i)
        if i in leave:
            count = leave.count(i)
            for j in range(count):
                min_cost += cost(N, i - available_tickets[-1])
                available_tickets.pop()
    return original_cost - min_cost

for no_test in range(1, total_test_case + 1):
    print("Case #%d: %d" % (no_test, solution()))