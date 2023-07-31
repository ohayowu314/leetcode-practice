# 0664. Strange Printer
There is a strange printer with the following two special properties:

- The printer can only print a sequence of **the same character** each time.
- At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.

Given a string `s`, return *the minimum number of turns the printer needed to print it*.

### **Constraints**:
- 1 <= `s.length` <= 100
- `s` consists of lowercase English letters.

### **Example 1**:

**Input**:

    (string) s = "aaabbb"

**Output**:

    (int) 2

**Explanation**:

    Print "aaa" first and then print "bbb".

### **Example 2**:

**Input**:

    (string) s = "aba"

**Output**:

    (int) 2

**Explanation**:

    Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.

### Similar Questions
- 0546 Remove Boxes: Hard
- 1591 Strange Printer II: Hard

### Related Topics
- String
- Dynamic Programming

# 理論解釋
先定義幾個符號 $s$ 代表函數的輸入字串，也是打印機最後要輸出的結果，稱為最終字串， $s_i$ 代表最終字串的第 $i^{th}$ 個字符(從0開始)， $s_{l..r}$ 代表最終字串從 $l$ 到 $r$ 之間的子字串(包含兩端)。

定義數對 $(c, l, r)$ 代表一次操作中將從 $l$ 到 $r$ 的字符修改成 $c$。可以通過減少每一次操作的 $r$ 從而證明必然存在一個最佳操作是由 $(s_r, l, r)$ 這樣的操作構成的；也就是說必然可以在每一次修改操作中，都使用要修改的位置中最後一個位置所對應的最終字符。

# 解題思路
先定義，對於給定的 $(l, r)$，由 $r-l+1$ 個最終字符 $s_r$ 組成的字串稱為 $t{(l,r)}$ 簡稱為 $t$，而由 $t$ 開始達到最終子字串 $s_{l..r}$ 所需的最小修改次數定為 $\text{dp}[l][r]$。

有上述理論後，我們可以以最終字串為標準，對於每一給定的 $(l, r)$， $\text{dp}[l][r]$ 都可以按照以下步驟拆解成更小的 $\text{dp}$ 構成。

1. 如果 $t$ 已經是最終子字串 $s_{l..r}$，也就是說最終子字串 $s_{l..r}$ 都由 $s_r$ 構成，不需修改，所以 $\text{dp}[l][r]=0$。這是 $\text{dp}$ 的基礎狀況/元素/情況/要素。
2. 否則最終子字串 $s_{l..r}$ 並非 $t$，必然存在最小的 $j\geq l$ 使得 $s_j\neq s_r$，按照 $t$, $j$ 的定義，這意味 $t_{l..j-1}$ 是不需要修正的，而 $j$ 這個位置是必定要修正的。所以我們假設下一個操作 $(s_i,j,i)$ 要從 $j$ 開始，但不知到哪個 $i$ 結束。那就跑遍所有可能的 $i\in[j,r)$： ($r$ 這個位置不需修正，因為 $t_r=s_r$)
   1. 對於給定的位置 $i$， $t$ 經過操作 $(s_i,j,i)$ 修正後變成三個段落: $t_{l..j-1}$, $t_{j..i}$, $t_{i+1..r}$。
   2. 前面說過 $t_{l..j-1}$ 已經正確，不需要修正。
   3. 操作 $(s_i,j,i)$ 之後， $t_{j..i}$ 恰好變成 $t(j,i)$，需要的操作數量正好是 $\text{dp}[j][i]$。
   4. 操作 $(s_i,j,i)$ 之後， $t_{i+1..r}$ 這段並沒有變化，依舊是 $t(i+1,r)$，需要的操作數量正好是 $\text{dp}[i+1][r]$。
   5. 別忘了 $(s_i,j,i)$ 也要記一次操作。
3. 跑遍所有的 $i$，計算出 $1+\text{dp}[j][i]+\text{dp}[i+1][r]$ 最小值，即得到 $\text{dp}[l][r]$。

上述拆解中，每一個長的子字串都要用到短的子字串，所以我們必須先算短的子字串，從長度 $length$ 最短的 1 開始。

因為 $length = r - l + 1$ 所以 $r = length + l - 1$。 $r$ 最大為 $n-1$，所以 $l$ 最大為 $n - length$。

接下來通過 $\text{dp}$ 計算出函數的答案，假設 $s$ 的長度為 $n$。無論如何第一步驟都是將最後一個最終字符 $s_{n-1}$ 打印 $n$ 次，也就是操作 $(s_{n-1},0,n-1)$。這樣題目就變成從 $t(0,n-1)$ 開始，到達最終字串 $s$，正好需要 $\text{dp}[0][n-1]$ 次操作。(刻意從這樣的第一步開始，剛好能進入前面理論證明的狀況，方便我們使用 $\text{dp}$)

也因此最終答案為 $\text{dp}[0][n-1]+1$。

# 演算法結構
在代碼中，為了清楚起見，我們使用 `left` 表示 `l`，`right` 表示 `r`。

1. 令 $n$ 為 $s$ 的長度。
2. 宣告大小為 $n \times n$ 的二維串列 $\text{dp}$。 由於我們要找的是最小值，因此我們將串列初始化為 $n$（一個足夠大的值，保證不小於答案）。
3. 將 $\text{length}$ （當前打印的長度）從 $1$ 迭代到 $n$。
   - $\text{left}$ 從 $0$ 迭代到 $n - \text{length}$。
     - 設 $\text{right} = \text{left} + \text{length} - 1$。
     - 設 $j = -1$。 它將是與 `s[right]` 不同的字符的最左邊索引。 $j = -1$ 意味著我們還沒有找到任何這樣的字符。
     - 此時我們已經固定了狀態 `(left, right)`。 如上所述，我們現在嘗試所有的 $i$。 $i$ 從 $\text{left}$ 到 $\text{right} - 1$ 迭代。
       - 如果 `s[i] != s[right]` 且 $j = -1$（之前沒有不同的字符），則設置 $j := i$（這是第一個不同的字符）。
       - 如果 $j \ne -1$，將 $\text{dp}[\text{left}][\text{right}]$ 更新為 $1 + \text{dp}[j][i] + \text{dp}[i + 1][\text{right}]$，如果它更小。
     - 如果 $j = -1$，代表子字串 $s_{l..r}$ 由相同的字符組成，設置 $\text{dp}[\text{left}][\text{right}] = 0$。 （DP 的基礎情況。）
4. 返回 $\text{dp}[0][n - 1] + 1$。

# **Solution**:
## Python3 Leetcode 提供:
### Approach 1: Bottom-Up Dynamic Programming
```py
class Solution:
    def strangePrinter(self, s: str) -> int:
        # get length of string
        n = len(s)

        # dp[l][r] is the number of minimum step from [s_r]*(length)=t(l,r) to s_{l..r}
        # initial dp with the largest possible value
        dp = [[n] * n for _ in range(n)]

        # we have to compute shorter substring first
        # length from shortest 1 to longest n
        for length in range(1, n + 1):
            # the largest right is n - 1 = left + length - 1
            # thus the largest left = n - length
            for left in range(n - length + 1):
                # length = right - left + 1 so right = left + length - 1
                right = left + length - 1

                # want to find the first different character from s_r
                j = -1
                for i in range(left, right):
                    # if not yet found diff and now find one
                    if s[i] != s[right] and j == -1:
                        # set j be the index of diff
                        j = i

                    # if already found diff
                    if j != -1:
                        # string t(left, right) to s_{l..r}
                        # after 1 step (s_i, j, i)
                        # substring t_{left, j-1} is same as s_{left, j-1} don't need change
                        # substring t_{j, i} is same as t(j, i), want change to s_{j, i}, need dp[j][i] step
                        # substring t_{i+1, right} is same as t(i+1, right), want change to s_{i+1, right}, need dp[i+1][right] step
                        # update dp[left][right] with 1 + dp[j][i] + dp[i + 1][right] if smaller
                        dp[left][right] = min(dp[left][right], 1 + dp[j][i] + dp[i + 1][right])

                # if not found diff after loop
                # means s_{l..r} consists of the same character
                # base case
                if j == -1:
                    dp[left][right] = 0

        # always do one step (s_{n-1},0,n-1) in the first to get t(0,n-1) string
        # and then need dp[0][n-1] step to s_{0..n-1}=s
        return dp[0][n - 1] + 1
```
#### Complexity Analysis
- Time complexity: $O(n^3)$.

There are three nested loops: `for length`, `for left`, `for i`. Since each of these loops performs $O(n)$ iterations, the total time complexity is $O(n^3)$.

- Space complexity: $O(n^2)$

We maintain a 2D array $\text{dp}$ of size $n \times n$.
#### Grade
- Runtime: 1358 ms Beats 34.19 %
- Memory: 16.4 MB Beats 92.90 %

### Approach 2: Top-Down Dynamic Programming (Memoization)
```py
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def solve(left, right):
            if dp[left][right] != -1:
                return dp[left][right]
            
            dp[left][right] = n
            j = -1
            
            for i in range(left, right):
                if s[i] != s[right] and j == -1:
                    j = i
                if j != -1:
                    dp[left][right] = min(dp[left][right], 1 + solve(j, i) + solve(i + 1, right))
                    
            if j == -1:
                dp[left][right] = 0
    
            return dp[left][right]

        return solve(0, n - 1) + 1
```
#### Complexity Analysis
- Time complexity: $O(n^3)$.

Even though we changed the order of calculating DP, the time complexity is the same as in the previous approach: for each `left, right`, we compute $\text{dp}[\text{left}][\text{right}]$ in $O(n)$. Since we store the results in memory, we will calculate each $\text{dp}[\text{left}][\text{right}]$ only once.

- Space complexity: $O(n^2)$

It is the same as in the first approach. The `dp` array we are using to cache results takes $O(n^2)$ space. We also use some stack space for the recursion, but it is dominated by `dp`.
#### Grade
- Runtime: 2136 ms Beats 12.90 %
- Memory: 17.4 MB Beats 50.97 %

## Python3 最快:
```py
class Solution:
	def strangePrinter(self, s: str) -> int:
		
		s = ''.join([c for i, c in enumerate(s)
					 if i == 0 or c != s[i - 1]])

		next_occ_search = {}
		next_occurrence_of_letter = list(range(len(s)))
		for i, c in enumerate(s):
			if c in next_occ_search:
				next_occurrence_of_letter[next_occ_search[c]] = i
			next_occ_search[c] = i

		for v in next_occ_search.values():
			next_occurrence_of_letter[v] = 10**10

		@functools.lru_cache(None)
		def dp(left_ind: int, right_ind: int) -> int:

			if left_ind >= right_ind:
				return 0

			if s[right_ind] == s[left_ind]:
				return dp(left_ind + 1, right_ind)

			ans = 1 + dp(left_ind + 1, right_ind)

			pivot_index = next_occurrence_of_letter[left_ind]
			while pivot_index <= right_ind:
				ans = min(ans, 1 + dp(left_ind + 1, pivot_index)
						  + dp(pivot_index + 1, right_ind))
				pivot_index = next_occurrence_of_letter[pivot_index]

			return ans

		s += '#'
		return dp(0, len(s) - 1)
        
```
#### Grade
- Runtime: 117 ms Beats 100 %
- Memory: 19.2 MB Beats 43.23 %

## Python3 最小:
```py
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = float('inf')
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

        return dp[0][n - 1]
```
#### Grade
- Runtime: 896 ms Beats 51.61 %
- Memory: 16.3 MB Beats 92.90 %