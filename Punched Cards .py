total_test_case = int(input())

def solution():
    R, C = map(int, input().split())
    first_line = []
    second_line = []
    odd_line = []
    even_line = []
    for i in range(2*C + 1):
        if (i == 0):
            first_line.append(".")
            second_line.append(".")
            odd_line.append("+")
            even_line.append("|")
        elif (i == 1):
            first_line.append(".")
            second_line.append(".")
            odd_line.append("-")
            even_line.append(".")
        elif (i % 2 == 1):
            first_line.append("-")
            second_line.append(".")
            odd_line.append("-")
            even_line.append(".")
        else:
            first_line.append("+")
            second_line.append("|")
            odd_line.append("+")
            even_line.append("|")

    str1 = ""
    for j in range(2*R + 1):
        if (j == 0):
            print(str1.join(first_line))
        elif (j == 1):
            print(str1.join(second_line))
        elif (j % 2 == 1):
            print(str1.join(even_line))
        else:
            print(str1.join(odd_line))

for no_test in range(1, total_test_case + 1):
    print("Case #%d: " % (no_test))
    solution()