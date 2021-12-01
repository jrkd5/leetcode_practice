class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')' : '(', 
                   '}' : '{', 
                   ']' : '['}
        brackets = []
        for c in s:
            if c in '({[':
                brackets.append(c)
            else:
                if not brackets or brackets.pop() != mapping[c]:
                    return False
        if brackets:
            return False
        else:
            return True


ss = Solution()
assert ss.isValid('()') == True
assert ss.isValid('(){}[]') == True
assert ss.isValid(')') == False
assert ss.isValid('([)]') == False