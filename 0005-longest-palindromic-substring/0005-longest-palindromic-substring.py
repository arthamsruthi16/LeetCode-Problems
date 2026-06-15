class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0] * n
        center = right = 0
        max_len = 0
        center_index = 0
        for i in range(n):
            mirror = 2 * center - i 
            if i < right:
                p[i] = min(right - i, p[mirror])
            a = i + p[i] + 1
            b = i - p[i] - 1
            while a < n and b >= 0 and t[a] == t[b]:
                p[i] += 1
                a += 1
                b -= 1
            if i + p[i] > right:
                center = i
                right = i + p[i]
            if p[i] > max_len:
                max_len = p[i]
                center_index = i
        start = (center_index - max_len) // 2
        return s[start: start + max_len]      