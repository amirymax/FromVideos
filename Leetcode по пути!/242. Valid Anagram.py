class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = sorted(s)
        str2 = sorted(t)
        return str1 == str2