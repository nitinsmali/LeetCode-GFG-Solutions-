class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
    
        for char in s:
            if char == ')':
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                
                if stack:
                    stack.pop()
                
                
                for c in temp:
                    stack.append(c)
            else:
                stack.append(char)
                
        return "".join(stack)