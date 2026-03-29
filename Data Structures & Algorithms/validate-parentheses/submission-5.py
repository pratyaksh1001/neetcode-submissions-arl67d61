class Solution:
    def isValid(self, st: str) -> bool:

        if len(st) % 2 != 0:
            return False

        s = []

        for i in st:
            if i in "([{":
                s.append(i)

            elif i == ')':
                if not s or s[-1] != '(':
                    return False
                s.pop()

            elif i == ']':
                if not s or s[-1] != '[':
                    return False
                s.pop()

            elif i == '}':
                if not s or s[-1] != '{':
                    return False
                s.pop()

        return len(s) == 0