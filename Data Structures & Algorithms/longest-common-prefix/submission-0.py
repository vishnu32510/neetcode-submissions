class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = []
        n = len(strs)
        min_str_len = min([len(s) for s in strs])
        for i in range(min_str_len):
            s = "" 
            for j in range(n):
                if s == "":
                    s = strs[j][i] 
                if strs[j][i] != s:
                    return "".join(longest)
            longest.append(s)
        return "".join(longest)

