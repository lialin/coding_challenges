# Author: Liang Lin
# Email: lianglin@outlook.com
# Date: 2016-09-17
def solution(S, P, Q):

        # the length of position array
        n = len(P)

        # convert string to list
        types = list(S)

        # type list length
        tLen = len(types)

        # create a two-dimensional array to count the number of each
        # individual type in the type list
        ts = []

        # contains the result
        results = []

        # update the two-dimensional array
        #
        # the nested array contains the type number and
        # the sum of the type number at the current index
        # e.g. [[2,1],[2,2],[1,1],[3,1]]
        # [2,1] 2 represents the type number,
        # 1 represents the sum of the type number at the current index
        for i in range(tLen):
            ts.append([])

        for i in range(4):
            type_counter = 0
            for j in range(tLen):
                if convert(types[j]) == i+1:
                    print types[j]
                    print convert(types[j])
                    type_counter += 1
                    ts[convert(types[j])].append(type_counter)
                    print(ts)

        print(ts)
        # count the types
        # for i in range(4):
        #     for j in range(tLen):
        #         if ts[j][0] == i:
        #             ts[j][1] += 1




def convert(Type):
        return {
            "A" : 1,
            "C" : 2,
            "G" : 3,
            "T" : 4
        }[Type]

# sol = Solution()
solution("CTAAGT", [2,5,0], [3,5,3])
