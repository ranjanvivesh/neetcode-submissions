class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oprandstack = []
        if not tokens:
            return 0
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                oprandstack.append(int(tokens[i]))
            else:
                b = oprandstack.pop()
                a = oprandstack.pop()
                if tokens[i] == '+':   
                    oprandstack.append(b+a)
                if tokens[i] == '-':
                    oprandstack.append(a-b)
                if tokens[i] == '*':
                    oprandstack.append(b*a)
                if tokens[i] == '/':
                    oprandstack.append(int(a/b))
        return oprandstack[0]            
                        