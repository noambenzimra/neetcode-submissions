class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =  s.lower()
        new_s =''
        for char in s:
            if char.isalnum():
                new_s = new_s + char
        r = len(new_s) - 1

        for l in range(len(new_s)//2):
            if new_s[l] != new_s[r]:
                return False
            r-=1
        return True