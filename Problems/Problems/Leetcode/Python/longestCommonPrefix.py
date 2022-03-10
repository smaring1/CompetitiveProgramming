class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur  = min(strs, key=len)
        for i in strs:
            for j in range(len(cur)):
                if i[j] != cur[j]:
                    cur = cur[:j]
                    break
        return cur