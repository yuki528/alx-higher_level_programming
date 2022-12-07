#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res = 0.0
    s_list = list(t[0] * t[1] for t in my_list)
    w_list = list(t[1] for t in my_list)
    res = sum(s_list) / sum(w_list)
    return res

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))
