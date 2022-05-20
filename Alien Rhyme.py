import copy

total_test_case = int(input())

def solution():
    no_word = int(input())
    lst = []
    for i in range(0, no_word):
        word = input()
        stringlength = len(word)
        word = word[stringlength::-1]
        lst.append(word)
    lst = sorted(lst, key=len, reverse = True)
    left = copy.deepcopy(lst)
    taken = []
    for i in range(0, no_word):
        if lst[i] not in left:
            continue
        for j in range(len(lst[i]) - 1, 0, -1):
            suffix = lst[i][:j]
            for k in range(0, len(left)):
                if left[k] == lst[i]:
                    continue
                new = left[k]
                if suffix == new[:j]:
                    if suffix not in taken:
                        taken.append(suffix)
                        left.remove(new)
                        left.remove(lst[i])
                        break
            if lst[i] not in left:
                break
    return 2*len(taken)

for no_test in range(1, total_test_case + 1):
    print("Case #%d: %s" % (no_test, solution()))