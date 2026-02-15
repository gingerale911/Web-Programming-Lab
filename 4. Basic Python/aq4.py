class ParenthesesValidator:
    def is_valid(self, s):
        stack = []
        pairs = {')':'(', '}':'{', ']':'['}
        
        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            elif ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
        return len(stack) == 0

validator = ParenthesesValidator()
s = input()
print("Valid" if validator.is_valid(s) else "Invalid")
