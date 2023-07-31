class Solution:
    # Memory Limit Exceeded
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)
        # input (i,j)
        # output (length, [(largestCommonSubSeq, deleteSum)])
        memo: dict[tuple[int,int], tuple[int, set[tuple[str, int]]]] = {}
        def solve(i:int, j:int, call=0) -> tuple[int, set[tuple[str, int]]]:
            # print("\t"*call, i,j, end=" ")
            if i <= 0 or j <= 0:
                # print(" ", (0,[("",sum(ord(c) for c in s1[:i]+s2[:j]))]))
                return (0,{("",sum(ord(c) for c in s1[:i]+s2[:j]))})

            if (i, j) in memo:
                # print(" ", memo[(i, j)])
                return memo[(i, j)]

            if s1[i - 1] == s2[j - 1]:
                # print("")
                length, possibleSet = solve(i-1,j-1,call+1)
                newpossibleSet = set([(lcss+s1[i-1], ds) for lcss, ds in possibleSet])
                memo[(i, j)] = (length+1, newpossibleSet)
            else:
                # print("")
                length1, possibleSet1 = solve(i-1,j,call+1)
                # print("")
                length2, possibleSet2 = solve(i,j-1,call+1)
                if length1 > length2:
                    length = length1
                    newpossibleSet = [(lcss, ds+ord(s1[i-1])) for lcss, ds in possibleSet1]
                elif length1 < length2:
                    length = length2
                    newpossibleSet = [(lcss, ds+ord(s2[j-1])) for lcss, ds in possibleSet2]
                else:
                    length = length1
                    newpossibleSet = [(lcss, ds+ord(s1[i-1])) for lcss, ds in possibleSet1]
                    newpossibleSet += [(lcss, ds+ord(s2[j-1])) for lcss, ds in possibleSet2]
                memo[(i, j)] = (length, set(newpossibleSet))
            # print("\t"*call, " "*5, memo[(i, j)])
            return memo[(i, j)]

        return min(val for _,val in solve(n1, n2)[1])

class Solution:
    # First AC
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)
        # input (i,j)
        # output (length, [(largestCommonSubSeq, deleteSum)])
        memo: dict[tuple[int,int], tuple[int, int]] = {}
        def solve(i:int, j:int, call=0) -> tuple[int, int]:
            # print("\t"*call, i,j, end=" ")
            if i <= 0 or j <= 0:
                # print(" ", (0, sum(ord(c) for c in s1[:i]+s2[:j])))
                return (0, sum(ord(c) for c in s1[:i]+s2[:j]))

            if (i, j) in memo:
                # print(" ", memo[(i, j)])
                return memo[(i, j)]

            if s1[i - 1] == s2[j - 1]:
                # print("")
                length, possible = solve(i-1,j-1,call+1)
                memo[(i, j)] = (length+1, possible)
            else:
                # print("")
                length1, possible1 = solve(i-1,j,call+1)
                # print("")
                length2, possible2 = solve(i,j-1,call+1)
                if length1 > length2:
                    length = length1
                    newpossible = possible1+ord(s1[i-1])
                elif length1 < length2:
                    length = length2
                    newpossible = possible2+ord(s2[j-1])
                else:
                    length = length1
                    newpossible = min(possible1+ord(s1[i-1]), possible2+ord(s2[j-1]))
                memo[(i, j)] = (length, newpossible)
            # print("\t"*call, " "*5, memo[(i, j)])
            return memo[(i, j)]

        return solve(n1, n2)[1]

class Solution:
    # more simple
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)
        # input (i,j)
        # output (length, [(largestCommonSubSeq, deleteSum)])
        memo: dict[tuple[int,int], int] = {}
        def solve(i:int, j:int) -> int:
            if i <= 0 and j <= 0:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i <= 0:
                memo[(i,j)] = ord(s2[j-1]) + solve(i, j-1)
                return memo[(i,j)]
            
            if j <= 0:
                memo[(i,j)] = ord(s1[i-1]) + solve(i-1, j)
                return memo[(i,j)]

            if s1[i - 1] == s2[j - 1]:
                memo[(i, j)] = solve(i-1,j-1)
            else:
                memo[(i, j)] = min(solve(i-1,j)+ord(s1[i-1]), solve(i,j-1)+ord(s2[j-1]))
            return memo[(i, j)]

        return solve(n1, n2)

if __name__ == '__main__':
    sol = Solution()
    print('Example 1:')
    print('Input: s1 = "sea", s2 = "eat"')
    print('Output:')
    print('{}'.format(sol.minimumDeleteSum(s1 = "sea", s2 = "eat")))
    print('Expected:')
    print('231')
    print('\n','-'*100,'\n')
    print('Example 2:')
    print('Input: s1 = "delete", s2 = "leet"')
    print('Output:')
    print('{}'.format(sol.minimumDeleteSum(s1 = "delete", s2 = "leet")))
    print('Expected:')
    print('403')