class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        n=len(s)
        m=len(t)
        if s==t:
            return True
        else:
            return False
            # for i in range(n):
            #     if s[i]!=t[i]:
            #         return False
            # return True