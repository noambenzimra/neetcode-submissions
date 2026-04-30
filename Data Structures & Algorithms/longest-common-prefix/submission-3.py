class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        strs.sort()
        print(strs)
        r = len(strs) - 1
        i = 0
        prefix = ''
        for char in strs[0]:
            if char == strs[r][i]:
                prefix = prefix + char
                i+=1
            else:
                return prefix
        return prefix


