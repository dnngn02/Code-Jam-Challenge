total_test_case = int(input())

def solution():
    test_case = int(input())
    path = input()
    result = []
    for move in path:
        if (move == "S"):
            result.append("E")
        else:
            result.append("S")
    return ''.join(result)

for no_test in range (1, total_test_case + 1):
    print("Case #%d: %s" % (no_test, solution()))

