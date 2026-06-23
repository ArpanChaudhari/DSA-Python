class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Method 1
        # cleaned="".join(ch.lower() for ch in s if ch.isalnum())
        # print(cleaned)
        
        # if cleaned == cleaned[::-1]:
        #     return True
        
        # return False

        # Method 2
        cleaned="".join(filter(str.isalnum,s))
        cleaned=cleaned.lower()
        return cleaned == cleaned[::-1]
    
s = "A man, a plan, a canal: Panama"
sol=Solution()
print(sol.isPalindrome(s))
    