total_test_case = int(input())

def solution():
    min_color =[10**6, 10**6, 10**6, 10**6]
    for i in range(3):
        s = (list(map(int, input().split())))
        min_color[0] = min(min_color[0], s[0])
        min_color[1] = min(min_color[1], s[1])
        min_color[2] = min(min_color[2], s[2])
        min_color[3] = min(min_color[3], s[3])
    color = []
    total = 10**6
    for i in range(4):
        used = min(min_color[i], total)
        color.append(used)
        total -= used
    if total > 0:
        return "IMPOSSIBLE"
    else:
        return ''.join(str(x) for x in color)

for no_test in range(1, total_test_case + 1):
    print("Case #%d:" % (no_test), end="")
    result = solution()
    print(''.join(result))