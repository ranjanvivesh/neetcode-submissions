
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ch in operations:
            if ch not in ["+","C","D",]:
                stack.append(int(ch))
            if ch == "+":
                self.summ(stack)
            if ch == "D":
                self.doub(stack)    
            if ch == "C":
                stack.pop()    
        return sum(stack)        
    def summ(self,stack):
        summs = stack[-1] + stack[-2]
        stack.append(summs)
    def doub(self,stack):
        stack.append(2*stack[-1])  