class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            # If characters match, just keep moving inward
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # Option 1: Skip the left character (s[l+1 : r+1])
                skip_l = s[l+1 : r+1]# skip only the left charachter
                
                skip_r = s[l : r]# skip only the right charachter
                
                return skip_l == skip_l[::-1] or skip_r == skip_r[::-1]
                
        return True