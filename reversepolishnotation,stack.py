4.reverse Polish notation
-------------------------------------------------------------------------------------
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators={'+':lambda x,y:x+y,'-':lambda x,y:y-x,'*':lambda x,y:x*y,'/':lambda x,y:int(y/x)} 
        l=0
        stack=[]
        if len(tokens)<=1:
            return int(tokens[0])
        while l<len(tokens):
            if tokens[l] not in operators:
                stack.append(tokens[l])
            else:
                curr=operators[tokens[l]](int(stack[-1]),int(stack[-2]))
                stack.pop()
                stack.pop()
                stack.append(int(curr))
            l+=1
        return stack[0]
