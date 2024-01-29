class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()
        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue 

            while not s[r].isalnum():
                r -= 1
                continue
            
            if s[l].isalnum() and s[r].isalnum():
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                    continue
                else:
                    return False
        
        return True

                
