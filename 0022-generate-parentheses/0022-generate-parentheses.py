class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]
        for k in range(1, n+1):
            for i in range(k):
                j = k - 1 - i
                for s_a in dp[i]:
                    for s_b in dp[j]:
                        dp[k].append(f"({s_a}){s_b}")
        return dp[n]