class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = self.str_to_int(a)
        print(num1)
        num2 = self.str_to_int(b)
        print(num2)
        res = num1 + num2

        res = self.int_to_str(res)
        if res == "":
            return str(0)
        return res

    def str_to_int (self, a:str) -> int:
        num = 0
        for i in range (len(a)):
            if a[i] == '1':
                power = len(a) - 1 - i
                num = num + 2**power
        return num
    
    def int_to_str (self, num: int) -> str:
        a = ''
        while num > 0:
            res = num % 2
            a = str(res) + a
            num = num // 2
        return a
        
        

                        