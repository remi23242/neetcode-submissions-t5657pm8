class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            if x.lstrip('-').isdigit():
                stack.append(int(x))
            else:
                second_val = stack.pop()
                first_val = stack.pop()

                if x == '+':
                    stack.append(first_val + second_val)
                elif x == '-':
                    stack.append(first_val - second_val)
                elif x == '*':
                    stack.append(first_val * second_val)
                elif x == '/':
                    stack.append(int(first_val / second_val))

        return stack[0]