class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        i = 0
        new_word = ''
        while n > 0 and m > 0:
            new_word = new_word + word1[i]
            new_word = new_word + word2[i]
            n-=1
            m-=1
            i+=1

        if n > 0:
            while n > 0:
                new_word = new_word+ word1[i]
                i+=1
                n-=1
        elif m > 0:
            while m > 0 :
                new_word = new_word + word2[i]
                i+=1
                m-=1
        return new_word
        





        n = len(word1)
        m = len(word2)
        res = []

        for i in range(max(n,m)):

            if i < n:
                res.append(word1[i])
            if i < m:
                res.append(word2[i])
        return "".join(res)


            
