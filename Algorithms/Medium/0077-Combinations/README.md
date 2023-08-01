# 0077. Combinations
Given two integers `n` and `k`, return *all possible combinations of `k` numbers chosen from the range `[1, n]`*.

You may return the answer in **any order**.

### **Constraints**:
- 1 <= `n` <= 20
- 1 <= `k` <= `n`

### Example 1:

**Input**:

    (int) n = 4, k = 2

**Output**:
    
    (array of array of int) 
    [
        [1,2],[1,3],[1,4],[2,3],[2,4],[3,4]
    ]

**Explanation**:
    
    There are 4 choose 2 = 6 total combinations.
    Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

### Example 2:

**Input**:

    (int) n = 1, k = 1

**Output**:
    
    (array of array of int) 
    [
        [1]
    ]

**Explanation**:

    There is 1 choose 1 = 1 total combination.

### Similar Questions
- 0039 Combination Sum: Medium
- 0046 Permutations: Medium
### Related Topics
- Backtracking

# **Solution**:
## Python3:
### 直接 AC
```py
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # use to store all answers
        ans = []
        # combination list that maybe a answer
        temp = []

        # i is the item we want put in comb list
        # t is the len of comb list
        def comb(i, t):
            # if len is k then comb list is full and be an answer
            if t == k:
                ans.append(temp[:])
                return
            # item out of range
            if i == n+1:
                return
            # comb list get the item
            temp.append(i)
            # try to add next item
            comb(i+1, t+1)
            # comb list don't get the item
            temp.remove(i)
            # try to add next item
            comb(i+1, t)
        comb(1,0)
        return ans
```
#### Complexity Analysis
- Time complexity: $O(C(n,k))=O(n \text{ choose } k)\approx O(\min(n^k, n^{n-k}))$.

$$\left(\frac{n}{k}\right)^k\leq {n \choose k} \leq \left(\frac{en}{k}\right)^k$$

- Space complexity: $O(C(n,k))$.
#### Grade
- Runtime: 427 ms Beats 27.67 %
- Memory: 18.2 MB Beats 90.6 %
### 第二次 設置斷點
如果從項目 i 到結尾 n 之間的數字根本無法將串列 temp 補足到 k 個數字，那麼根本不用嘗試 i 到 n 之間的數字，可以直接回頭。
```py
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        temp = []
        def pick(i, t):
            if t == k:
                ans.append(temp[:])
                return
            # if numbers in i..n can't fill temp to k
            # we can break immediately
            if k-t+i-1>n:
                return
            if i == n+1:
                return
            temp.append(i)
            pick(i+1, t+1)
            # here can use pop since the new item always add in tail
            temp.pop()
            pick(i+1, t)
        pick(1,0)
        return ans
```
複雜度不分析了，因為都差不多
#### Grade
- Runtime: 80 ms Beats 98.92 %
- Memory: 18.2 MB Beats 90.6 %
### 第三次 直接用長度取代 t
```py
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        temp = []
        def pick(i):
            if len(temp) == k:
                ans.append(temp[:])
                return
            if k-len(temp)+i-1>n:
                return
            if i == n+1:
                return
            temp.append(i)
            pick(i+1)
            temp.pop()
            pick(i+1)
        pick(1)
        return ans
```
#### Grade
- Runtime: 78 ms Beats 99.15 %
- Memory: 18.2 MB Beats 67.82 %

## Python3 Leetcode 提供 要付費

## Python3 最快:
```py
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations(range(1,n+1),k)
```
#### Complexity Analysis
- Time complexity: $??$ depend on itertools.combinations.
- Space complexity: $??$.

#### Grade
- Runtime: 63 ms Beats 99.94 %
- Memory: 17.1 MB Beats 99.64 %

## Python3 最小:
```py
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations(range(1,n+1),k)
```
#### Complexity Analysis
- Time complexity: $??$ depend on itertools.combinations.
- Space complexity: $??$.

#### Grade
- Runtime: 63 ms Beats 99.94 %
- Memory: 17.1 MB Beats 99.64 %