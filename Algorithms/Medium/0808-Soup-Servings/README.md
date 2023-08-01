# 0808. Soup Servings
There are two types of soup: **type A** and **type B**. Initially, we have `n` ml of each type of soup. There are four kinds of operations:

1. Serve `100` ml of **soup A** and `0` ml of **soup B**,
2. Serve `75` ml of **soup A** and `25` ml of **soup B**,
3. Serve `50` ml of **soup A** and `50` ml of **soup B**, and
4. Serve `25` ml of **soup A** and `75` ml of **soup B**.


When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal probability `0.25`. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.

### **Note**:
that we do not have an operation where all `100` ml's of **soup B** are used first.

Return *the probability that **soup A** will be empty first, plus half the probability that **A** and **B** become empty at the same time*. Answers within $10^{-5}$ of the actual answer will be accepted.

### **Constraints**:
- 0 <= `n` <= $10^9$

### **Example 1**:
**Input**:

    (int) n = 50

**Output**:

    (float) 0.62500

**Explanation**:

    If we choose the first two operations, A will become empty first.
    For the third operation, A and B will become empty at the same time.
    For the fourth operation, B will become empty first.
    So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

### **Example 2**:
**Input**:

    (int) n = 100

**Output**:

    (float) 0.71875

### Related Topics
- Math
- Dynamic Programming
- Probability and Statistics

# **Solution**:
## Python3:
### 我第一個 AC 回答
```py
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
```
#### Complexity Analysis
- Time complexity: $O(1)$.

Let $\epsilon$ be the error tolerance, and $m_0$ be the first value such that $\text{dp}[m_0][m_0] > 1 - \epsilon$.

We calculate $O(\min(m, m_0) ^ 2) = O(m_0 ^ 2)$ states of DP in $O(1)$ each, meaning the total time complexity of the solution is $O(m_0 ^ 2)$.

We assume $\epsilon$ to be constant. It implies that $m_0$ is also constant, thus $O(m_0 ^ 2) = O(1)$. In our case, $\epsilon$ is $10^{-5}$, which gives us $m_0 \approx 200$.

- Space complexity: $O(1)$.

The space complexity is $O(m_0 ^ 2) = O(1)$.

#### Grade
- Runtime: 51ms Beats 80.19%
- Memory: 16.9MB Beats 87.74%
## Python3 Leetcode 提供:

### Approach 1: Bottom-Up Dynamic Programming
```py
class Solution:
    def soupServings(self, n: int) -> float:
        m = ceil(n / 25)
        dp = {}

        def calculate_dp(i, j):
            return (dp[max(0, i - 4)][j] + dp[max(0, i - 3)][j - 1] +
                    dp[max(0, i - 2)][max(0, j - 2)]
                    + dp[i - 1][max(0, j - 3)]) / 4

        dp[0] = {0: 0.5}
        for k in range(1, m + 1):
            dp[0][k] = 1
            dp[k] = {0: 0}
            for j in range(1, k + 1):
                dp[j][k] = calculate_dp(j, k)
                dp[k][j] = calculate_dp(k, j)
            if dp[k][k] > 1 - 1e-5:
                return 1
        return dp[m][m]
```
#### Complexity Analysis
- Time complexity: $O(1)$.

Let $\epsilon$ be the error tolerance, and $m_0$ be the first value such that $\text{dp}[m_0][m_0] > 1 - \epsilon$.

We calculate $O(\min(m, m_0) ^ 2) = O(m_0 ^ 2)$ states of DP in $O(1)$ each, meaning the total time complexity of the solution is $O(m_0 ^ 2)$.

We assume $\epsilon$ to be constant. It implies that $m_0$ is also constant, thus $O(m_0 ^ 2) = O(1)$. In our case, $\epsilon$ is $10^{-5}$, which gives us $m_0 \approx 200$.

- Space complexity: $O(1)$.

The space complexity is $O(m_0 ^ 2) = O(1)$.
#### Grade
- Runtime: 473 ms Beats 9.91%
- Memory: 18.8 MB Beats 24.53%
### Approach 2: Top-Down Dynamic Programming (Memoization)
```py
class Solution:
    def soupServings(self, n: int) -> float:
        m = ceil(n / 25)
        dp = collections.defaultdict(dict)

        def calculate_dp(i: int, j: int) -> float:
            if i <= 0 and j <= 0:
                return 0.5
            if i <= 0:
                return 1.0
            if j <= 0:
                return 0.0
            if i in dp and j in dp[i]:
                return dp[i][j]

            dp[i][j] = (
                calculate_dp(i - 4, j)
                + calculate_dp(i - 3, j - 1)
                + calculate_dp(i - 2, j - 2)
                + calculate_dp(i - 1, j - 3)
            ) / 4.0
            return dp[i][j]

        for k in range(1, m + 1):
            if calculate_dp(k, k) > 1 - 1e-5:
                return 1.0
        return calculate_dp(m, m)
```
#### Complexity Analysis
- Time complexity: $O(1)$.
- Space complexity: $O(1)$.

Both time and space complexities are the same as in the first approach.

#### Grade
- Runtime: 253 ms Beats 18.87%
- Memory: 23.8 MB Beats 12.74%
## Python3 最快:
```py
class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1
        @cache
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            return 0.25 * (dp(a-100, b) + dp(a-75, b-25) + dp(a-50, b-50)+ dp(a-25,b-75))
        x = dp(n, n)
        return x
```
#### Grade
- Runtime: 30 ms Beats 100%
- Memory: 17.2 MB Beats 51.42%
## Python3 最小:
```py
class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1
        stack = {(n,n):1}
        dirs = {(100,0),(75,25),(50,50),(25,75)}
        ans = 0
        while stack:
            new = defaultdict(float)
            for a,b in stack:
                t = stack[a,b] * 0.25
                if t < 0.00000001:
                    continue
                for x,y in dirs:
                    a0,b0 = a - x, b - y
                    if a0 > 0 and b0 > 0:
                        new[a0,b0] += t
                    elif a0 <= 0 and b0 > 0:
                        ans += t
                    elif a0 <= 0 and b0 <= 0:
                        ans += t / 2
            stack = dict(new)
        return ans
```
#### Grade
- Runtime: 40 ms Beats 98.58%
- Memory: 16.2 MB Beats 98.58%