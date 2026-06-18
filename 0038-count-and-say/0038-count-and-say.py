class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            i, temp = 0, []
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                temp.append(str(count))
                temp.append(s[i])
                i += 1
            s = ''.join(temp)
        return s
