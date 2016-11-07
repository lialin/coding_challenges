# Author: Liang Lin
# Email: lianglin@outlook.com
# Date: 2016-09-17

def solution(S, P, Q):
    # length of P
    pl = len(P)

    # convert S into list
    s_list = list(S)
    slen  = len(s_list)

    # create a list to count the types in s_list
    count_list = [[0 for i in range(slen+1)] for j in range(4)]

    # result list
    result_list = []

    for i in range(slen):
        factor = typeToFactor(s_list[i])
        count_list[factor][i+1] = 1

    # count the factors
    for i in range(4):
        for j in xrange(1,slen+1):
            count_list[i][j] += count_list[i][j-1]

    # find the minimal impact factor in s_list
    for i in range(pl):
        for j in range(4):
            if(count_list[j][Q[i]+1] - count_list[j][P[i]] > 0):
                result_list.append(j + 1)
                break
    return result_list

# convert type to factor
def typeToFactor(type):
    return {
        'A' : 0,
        'C' : 1,
        'G' : 2,
        'T' : 3
    }[type]
