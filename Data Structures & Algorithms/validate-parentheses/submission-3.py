class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'}':'{',']':'[',')':'('}
        stack = []
        for bracket in s:
            if bracket not in mapping:
                stack.append(bracket)
            elif mapping[bracket]:# return true if this is a closing bracket because if its not it will not find this key
                if not stack or stack[-1] != mapping[bracket]:# the last parenthese is not a oppening bracket it returns false , or the stack is empty so we dont have a openning one to our closed one
                    return False
                else:
                    stack.pop()
        return not stack #if the stack is empty itll return true, if the stack is not empty it means that we didnt find the closing parenthese
        
