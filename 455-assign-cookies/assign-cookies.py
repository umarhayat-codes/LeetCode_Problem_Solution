class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        i = 0
        j = 0
        content_child = 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                content_child += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return content_child
