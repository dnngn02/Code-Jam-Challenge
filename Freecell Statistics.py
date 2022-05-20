total_test_case = int(input())

def solution():
    set_of_no = input().split()
    N = int(set_of_no[0])
    Pd = int(set_of_no[1])
    Pg = int(set_of_no[2])
    if Pd == 0 and Pg == 0:
        return "Possible"
    elif Pd == 100 and Pg == 100:
        return "Possible"
    elif Pd < 100 and Pg == 100:
        return "Broken"
    elif Pd > 0 and Pg == 0:
        return "Broken"
    else:
        for d in range(1, N + 1):
            if d >= 101:
                break
            elif (d * Pd) % 100 == 0:
                return "Possible"
        return "Broken"

for no_test in range(1, total_test_case + 1):
    print("Case #%d: %s" % (no_test, solution()))