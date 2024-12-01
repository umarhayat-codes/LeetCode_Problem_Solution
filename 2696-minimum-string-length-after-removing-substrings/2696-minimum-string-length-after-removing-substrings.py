class Solution:
    def minLength(self,s):
        stack = []
        for i in s:
            if stack:
                if stack[-1] == "A" and i == "B":
                    stack.pop()
                    continue
                elif stack[-1] == "C" and i == "D":
                    stack.pop()
                    continue
            stack.append(i)
        return len(stack)
obj = Solution()
print(obj.minLength("ABFCACDB"))

