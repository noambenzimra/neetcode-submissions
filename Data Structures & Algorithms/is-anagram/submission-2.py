class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       s_sorted = sorted(s)
       t_sorted = sorted (t)
       return s_sorted == t_sorted

       if len(s) != len(t):
        return False

        count = [0] * 26 # creates an array with a size of 26 that have only zeros 

        for i in range(len(t)):
            count[s[i]- ord('a')] +=1
            count[t[i]- ord('a')] -=1
        for val in count:
            if val !=0:
                return False
        return True
