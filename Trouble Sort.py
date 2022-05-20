total_test_case = int(input())

def solution():
    length = int(input())
    set = list(map(int, input().split()))
    odd = []
    even = []
    for i in range (0, length):
        if i % 2 == 0:
            even.append(set[i])
        else:
            odd.append(set[i])
    odd.sort()
    even.sort()
    prev = even[0]
    for k in range(1, length):
        if k % 2 == 0:
            index = int(k/2)
            if prev > even[index]:
                return k - 1
            else:
                prev = even[index]
        else:
            index = int((k-1)/2)
            if prev > odd[index]:
                return k - 1
            else:
                prev = odd[index]
    return "OK"

for no_test in range(1, total_test_case + 1):
    print("Case #%d: %s" % (no_test, solution()))