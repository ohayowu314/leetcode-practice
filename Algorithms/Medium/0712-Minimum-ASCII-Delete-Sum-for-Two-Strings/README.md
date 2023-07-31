# 0712. Minimum ASCII Delete Sum for Two Strings
Given two strings `s1` and `s2`, return *the lowest **ASCII** sum of deleted characters to make two strings equal*.

### **Constraints**:
- 1 <= `s1.length`, `s2.length` <= 1000
- `s1` and `s2` consist of lowercase English letters.

### **Example 1**:
**Input**:

    (string) s1 = "sea", s2 = "eat"

**Output**:

    (int) 231

**Explanation**:
    
    Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
    Deleting "t" from "eat" adds 116 to the sum.
    At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
### **Example 2**:
**Input**:

    (string) s1 = "delete", s2 = "leet"

**Output**:

    (int) 403

**Explanation**:

    Deleting "dee" from "delete" to turn the string into "let", adds 100[d] + 101[e] + 101[e] to the sum.
    Deleting "e" from "leet" adds 101[e] to the sum.
    At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
    If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.

### Similar Questions
- 0072 Edit Distance: Medium
- 0300 Longest Increasing Subsequence: Medium
- 0583 Delete Operation for Two Strings: Medium
### Related Topics
- String
- Dynamic Programming

# **Solution**:
## Python3:
我第一個 AC 回答
```py
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
```
更簡單的回答
```py
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
```
#### Complexity Analysis
- Time complexity: $O(M \cdot N)$.
There will be at most $(M + 1) \cdot (N + 1)$ combination of `(i, j)` pair. Thus, the function `solve` will be called at most $(M + 1) \cdot (N + 1)$ times.

Each call to `solve` takes $O(1)$ time.

Hence, the time complexity is $O(M \cdot N)$.

- Space complexity: $O(M \cdot N)$.

There will be at most $(M + 1) \cdot (N + 1)$ entries in the hash map. Both `i` and `j` have one more possible value, which is `0`.<br>
*(The `i <= 0` simply means `i == 0` and `j <= 0` simply means `j == 0`. They won't be less than 0, because once any index is zero, we don't call the function `solve` with negative indices.)*.

Hence, the space complexity is $O(M \cdot N)$.

#### Grade
- Runtime: 1080 ms Beats 30.46 %
- Memory: 221.7 MB Beats 7.5 %


## Python3 Leetcode 提供:

### Approach 1: Recursion
Time Limit Exceeded
```py
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        # Return minimum cost to make s1[0...i] and s2[0...j] equal
        def compute_cost(i, j):

            # If s1 is empty, then we need to delete all characters of s2
            if i < 0:
                delete_cost = 0
                for pointer in range(j+1):
                    delete_cost += ord(s2[pointer])
                return delete_cost
            
            # If s2 is empty, then we need to delete all characters of s1
            if j < 0:
                delete_cost = 0
                for pointer in range(i+1):
                    delete_cost += ord(s1[pointer])
                return delete_cost
            
            # Check s1[i] and s2[j]
            if s1[i] == s2[j]:
                return compute_cost(i-1, j-1)
            else:
                return min(
                    ord(s1[i]) + compute_cost(i-1, j),
                    ord(s2[j]) + compute_cost(i, j-1),
                    ord(s1[i]) + ord(s2[j]) + compute_cost(i-1, j-1)
                )
        
        # Call helper function for complete strings
        return compute_cost(len(s1)-1, len(s2)-1)
```
#### Complexity Analysis
Let `s` be the longer string between `s1` and `s2`. Let $K$ be the length of `s`.

- Time complexity: $O(3^{K} \cdot K)$.

For each character of `s`, we recursively explore three possibilities. Either we can delete this character from `s`, or from another string, or we can delete both characters. Thus, we have three recursive calls for each character of `s`. Hence, there will be $3^{K}$ recursive calls.

The time complexity of each recursive call is $O(K)$ because we may need to traverse the complete string to calculate the cost.

Thus, the total time complexity will be $O(3^{K} \cdot K)$.

- Space complexity: $O(K)$.

The space complexity will be $O(K)$ because of the recursion stack. The recursive process will terminate when either of the strings becomes empty. Thus, the maximum depth of the recursion tree will be $K$.

#### Grade
- Runtime: Time Limit Exceeded
- Memory: Time Limit Exceeded

### Approach 2: Top-down Dynamic Programming
```py
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
    
        # Dictionary to store the result of each sub-problem
        saved_result = {}

        # Return minimum cost to make s1[0...i] and s2[0...j] equal
        def compute_cost(i, j):

            # If both strings are empty, then no deletion is required
            if i < 0 and j < 0:
                return 0
            
            # If already computed, then return the result from the dictionary
            if (i, j) in saved_result:
                return saved_result[(i, j)]
            
            # If any one string is empty, delete all characters of the other string
            if i < 0:
                saved_result[(i, j)] = ord(s2[j]) + compute_cost(i, j-1)
                return saved_result[(i, j)]
            if j < 0:
                saved_result[(i, j)] = ord(s1[i]) + compute_cost(i-1, j)
                return saved_result[(i, j)]
            
            # Call sub-problem depending on s1[i] and s2[j]
            # Save the computed result.
            if s1[i] == s2[j]:
                saved_result[(i, j)] = compute_cost(i-1, j-1)
            else:
                saved_result[(i, j)] = min(
                    ord(s1[i]) + compute_cost(i-1, j),
                    ord(s2[j]) + compute_cost(i, j-1)
                )

            return saved_result[(i, j)]

        # Return the result of the main problem
        return compute_cost(len(s1)-1, len(s2)-1)
```
#### Complexity Analysis
- Time complexity: $O(M \cdot N)$.
There will be at most $(M + 1) \cdot (N + 1)$ combination of `(i, j)` pair. Thus, the function `computeCost` will be called at most $(M + 1) \cdot (N + 1)$ times.

Each call to `computeCost` takes $O(1)$ time.

Hence, the time complexity is $O(M \cdot N)$.

- Space complexity: $O(M \cdot N)$.

There will be at most $(M + 1) \cdot (N + 1)$ entries in the hash map. Both `i` and `j` have one more possible value, which is `-1`.
*(The `i < 0` simply means `i == -1` and `j < 0` simply means `j == -1`. They won't be less than `-1`, because once any index is negative, we don't call the function `computeCost` with further negative indices.)*.

Hence, the space complexity is $O(M \cdot N)$.

#### Grade
- Runtime: 1054 ms Beats 32.17 %
- Memory: 221.6 MB Beats 8.52 %

### Appraoch 2 變化: 先把 base case 算完
```py
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        # Pre-compute sum of ASCII values of s1
        m = len(s1)
        s1_ascii_sum = [0] * m
        s1_ascii_sum[0] = ord(s1[0])
        for i in range(1, m):
            s1_ascii_sum[i] = ord(s1[i]) + s1_ascii_sum[i-1]

        # Pre-compute sum of ASCII values of s2
        n = len(s2)
        s2_ascii_sum = [0] * n
        s2_ascii_sum[0] = ord(s2[0])
        for i in range(1, n):
            s2_ascii_sum[i] = ord(s2[i]) + s2_ascii_sum[i-1]
        
        # Dictionary to store the result of each sub-problem
        saved_result = {}

        # Return minimum cost to make s1[0...i] and s2[0...j] equal
        def compute_cost(i, j):

            # If both strings are empty, then no deletion is required
            if i < 0 and j < 0:
                return 0
            
            # If any one string is empty, delete all characters of the other string
            if i < 0:
                return s2_ascii_sum[j]
            if j < 0:
                return s1_ascii_sum[i]
            
            # If already computed, then return the result
            if (i, j) in saved_result:
                return saved_result[(i, j)]
            
            # Call sub-problem depending on s1[i] and s2[j]
            # Save the computed result.
            if s1[i] == s2[j]:
                saved_result[(i, j)] = compute_cost(i-1, j-1)
                return saved_result[(i, j)]
            else:
                saved_result[(i, j)] = min(
                    ord(s1[i]) + compute_cost(i-1, j),
                    ord(s2[j]) + compute_cost(i, j-1)
                )
                return saved_result[(i, j)]
        
        # Return minimum deletion cost
        return compute_cost(m-1, n-1)
```

#### Complexity Analysis
- Time complexity: $O(M \cdot N)$.
Preparing `s1_ascii_sum` takes $O(M)$ time, and preparing `s2_ascii_sum` takes $O(N)$ time. Next, we call the `computeCost` function. This will be called $O(M \cdot N)$ times because there will be $O(M \cdot N)$ unique pairs of `(i, j)`. In each call, we do constant work. So, the total time complexity is $O(M + N + M \cdot N) = O(M \cdot N)$.

- Space complexity: $O(M \cdot N)$.

We use $O(M)$ space for `s1_ascii_sum`, $O(N)$ space for `s2_ascii_sum`, and O(M⋅N)O(M \cdot N)O(M⋅N) space for `savedResult` array. Hence, total space complexity is $O(M + N + M \cdot N) = O(M \cdot N)$.

#### Grade
- Runtime: 1026 ms Beats 33.53 %
- Memory: 217.7 MB Beats 16.71 %

### Approach 3: Bottom-up Dynamic Programming
```py
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        # Prepare the two-dimensional array
        m, n = len(s1), len(s2)
        compute_cost = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the base case values
        for i in range(1, m + 1):
            compute_cost[i][0] = compute_cost[i-1][0] + ord(s1[i-1])
        for j in range(1, n + 1):
            compute_cost[0][j] = compute_cost[0][j-1] + ord(s2[j-1])
        
        # Fill the remaining cells using the Bellman Equation
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    compute_cost[i][j] = compute_cost[i-1][j-1]
                else:
                    compute_cost[i][j] = min(
                        ord(s1[i-1]) + compute_cost[i-1][j],
                        ord(s2[j-1]) + compute_cost[i][j-1]
                    )
        
        # Return the answer for entire input strings
        return compute_cost[m][n]
```
#### Complexity Analysis
- Time complexity: $O(M \cdot N)$.
We are filling the `computeCost` array of size $(M + 1) \cdot (N + 1)$ in a row-wise fashion. For each cell, we are performing constant work. So, the time complexity is $O((M + 1) \cdot (N + 1))$ which using the asymptotic notation is $O(M \cdot N)$.

- Space complexity: $O(M \cdot N)$.

We are using a two-dimensional `computeCost` array of size $(M + 1) \cdot (N + 1)$ to store the intermediate results. So, the space complexity is $O((M + 1) \cdot (N + 1))$ which using the asymptotic notation is $O(M \cdot N)$.

#### Grade
- Runtime: 482 ms Beats 86.37 %
- Memory: 21 MB Beats 47.5 %

### Approach 4: Space-Optimized Bottom-up Dynamic Programming
```py
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        # Make sure s2 is smaller string
        if len(s1) < len(s2):
            return self.minimumDeleteSum(s1 = s2, s2 = s1)
        
        # Case for empty s1
        m, n = len(s1), len(s2)
        curr_row = [0] * (n + 1)
        for j in range(1, n + 1):
            curr_row[j] = curr_row[j - 1] + ord(s2[j - 1])
        
        # Compute answer row-by-row
        for i in range(1, m + 1):
            
            diag = curr_row[0]
            curr_row[0] += ord(s1[i - 1])

            for j in range(1, n + 1):
                
                # If characters are the same, the answer is top-left-diagonal value
                if s1[i - 1] == s2[j - 1]:
                    answer = diag
                
                # Otherwise, the answer is minimum of top and left values with
                # deleted character's ASCII value
                else:
                    answer = min(
                        ord(s1[i - 1]) + curr_row[j],
                        ord(s2[j - 1]) + curr_row[j - 1]
                    )

                # Before overwriting curr_row[j] with the answer, save it in diag
                # for the next column
                diag = curr_row[j]
                curr_row[j] = answer
        
        # Return answer
        return curr_row[-1]
```
#### Complexity Analysis
- Time complexity: $O(M \cdot N)$.

There are two nested for loops, thus there will be $M \cdot N$ iterations. In each iteration, we are doing constant work. Thus, the time complexity is $O(M \cdot N)$.

- Space complexity: $O(\min(M, N))$.

We are using a one-dimensional array of size $\min(M, N) + 1$ to store the current row. Thus, the space complexity is $O(\min(M, N))$.

#### Grade
- Runtime: 447 ms Beats 95 %
- Memory: 16.4 MB Beats 95.11 %

## Python3 最快:
```py
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [0] * len(s2)
        for c1 in s1:
            prev = 0
            for i, c2 in enumerate(s2):
                last = dp[i]
                if c1 == c2:
                    dp[i] = prev + ord(c1)
                if prev <= last:
                    prev = last
        return sum(map(ord, f'{s1}{s2}')) - 2 * max(dp)
```
#### Complexity Analysis
- Time complexity: $O(M \cdot N)$.
- Space complexity: $O(M + N)$.

#### Grade
- Runtime: 121 ms Beats 100 %
- Memory: 16.5 MB Beats 91.25 %

## Python3 最小:
```py
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        ascii_sum = sum(ord(i) for i in s1+s2)  
        dp = [ascii_sum] * (len(s2) + 1)

        for i in range(1, len(s1)+1):
            uniq = ""
            prev_rc = dp[0] 
            
            for j in range(1, len(s2)+1):
                prev_r = dp[j]
                
                dp[j] = min(prev_rc, 
                            dp[j-1] if s2[j-1] != uniq else prev_rc)
                    
                if s1[i-1] == s2[j-1]:
                    dp[j] -= ord(s1[i-1]) + ord(s2[j-1])
                    uniq = s1[i-1]

                dp[j] = min(dp[j], prev_r)

                prev_rc = prev_r

        return dp[-1]
```
#### Complexity Analysis
- Time complexity: $O(M \cdot N)$.
- Space complexity: $O(M + N)$.

#### Grade
- Runtime: 502 ms Beats 84.9 %
- Memory: 16.2 MB Beats 99.77 %