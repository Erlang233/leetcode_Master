# LC 20,LC1047,LC150
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(',
                '}':'{',
                ']':'['}

        stack = []
        for i in s:
            if i in {'{','[','('}: 
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False

‘’‘比较简单，但是可以用下in这个operator，平常很少用’‘’

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)


        return ''.join(stack)

删除相邻的重复项

‘’‘逆波兰表达式求值，理解后序计算‘’‘
class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in {'+','-','*','/'}:
                # Pop two elements
                b = stack.pop()
                a = stack.pop()
                # Perform the operation
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Use integer division that truncates towards zero
                    stack.append(int(a / b))
            else:
                # Push the number onto the stack
                stack.append(int(token))
        
        return stack.pop()

