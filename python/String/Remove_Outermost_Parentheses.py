'''
1021. Remove Outermost Parentheses
Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
'''
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        balance = 0
        start = 0

        for i, ch in enumerate(s):
            if ch == '(':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                res.append(s[start + 1:i])
                start = i + 1
        return ''.join(res)

sol=Solution()
print(sol.removeOuterParentheses("(()())(())"))
