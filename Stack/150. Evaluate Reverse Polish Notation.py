class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif i == '/':
                a,b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(i))
        
        return stack[0]

        # Time: O(n)
        # Memory: O(n)
