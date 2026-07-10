class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in mapping.values():
                stack.append(c)
            elif c in mapping:
                if not stack or mapping[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                return False
        
        return not stack