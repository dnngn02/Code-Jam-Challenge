total_test_case = int(input())

def solution(n):
    number = str(n)
    prev = "0"
    index = 0
    for digit in number:
        if digit < prev:
            left_part = str(int(number[:index])-1)
            right_part = "9" * (len(number) - index)
            return solution(left_part + right_part)
        index += 1
        prev = digit
    return int(number)

for no_test in range(1, total_test_case + 1):
    print("Case #%d: %s" % (no_test, solution(input())))