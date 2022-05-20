total_test_case = input()

def solution():
    word = input()
    l = len(word)
    double = []
    hold = []
    lhold = 0
    for i in range(0, l):
        if i == l - 1:
            double.append(word[i])
            return "".join(double)
        if word[i] == word[i+1]:
            double.append(word[i])
            lhold += 1
            hold.append(word[i])
        else:
            if lhold > 0:
                if hold[-1] < word[i+1]:
                    for j in range(0, lhold):
                        double.append(hold[-1])
                else:
                    lhold -= lhold
            if (word[i + 1] > word[i]):
                for j in range(0, 2):
                    double.append(word[i])
            else:
                double.append(word[i])

for no_test in range (1, int(total_test_case) + 1):
    print("Case #%d: %s" % (no_test, solution()))