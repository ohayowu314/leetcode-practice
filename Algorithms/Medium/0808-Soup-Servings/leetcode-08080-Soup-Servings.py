import math
class Solution:
    # 採用 動態規劃 memoization?
    def soupServings(self, n: int) -> float:
        # 每 25 ml 為一份
        m = math.ceil(n/25)
        
        # 答案對於 n 或 m 是遞增函數，當 m >= 200 答案近似 1
        # 因為題目對準確率要求只到 10^-5 可以直接回答 1
        if m >= 200:
            return 1
        
        # Memory array dp[i][j] 是當 A 剩餘i分 B 剩餘j分 時 A 獲勝的機率
        dp = [[0]*(m+1) for _ in range(m+1)]

        # 直接結束的部分
        for i in range(m+1):
            dp[0][i] = 1 # A 直接獲勝
            dp[i][0] = 0 # B 直接獲勝
        dp[0][0] = 0.5 # 平手

        # 迴圈計算每一步答案
        for i in range(1,m+1):
            for j in range(1,m+1):
                # 每一步有四種選擇
                dp[i][j] = 1/4*(
                    dp[max(0,i-4)][j]              # A 掏出 100 ml B 掏出  0 ml
                    +dp[max(0,i-3)][j-1]           # A 掏出  75 ml B 掏出 25 ml
                    +dp[max(0,i-2)][max(0,j-2)]    # A 掏出  50 ml B 掏出 50 ml
                    +dp[i-1][max(0,j-3)]           # A 掏出  25 ml B 掏出 75 ml
                )
        
        # 回傳答案
        return dp[m][m]

if __name__ == '__main__':
    sol = Solution()
    print('Example 1:')
    print('Input: n = 50')
    print('Output:')
    print('{:.5f}'.format(sol.soupServings(n = 50)))
    print('Expected:')
    print('0.62500')
    print('\n','-'*100,'\n')
    print('Example 2:')
    print('Input: n = 100')
    print('Output:')
    print('{:.5f}'.format(sol.soupServings(n = 100)))
    print('Expected:')
    print('0.71875')