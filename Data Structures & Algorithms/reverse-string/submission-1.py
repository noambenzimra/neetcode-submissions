class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        r = len(s) - 1

        for l in range(len(s) // 2):
            temp_left = s[l]
            s[l] = s[r]
            s[r] = temp_left
            r-=1 



        