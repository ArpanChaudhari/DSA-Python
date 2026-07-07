class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = [] # as string is immutable in python
        w1=0
        w2=0
        while w1 < len(word1) and w2 < len(word2):
            output.append(word1[w1])
            w1+=1
            output.append(word2[w2])
            w2+=1
        
        while w1 < len(word1):
            output.append(word1[w1])
            w1+=1

        while w2 < len(word2):
            output.append(word2[w2])
            w2+=1
        
        return "".join(output)
    
sol= Solution()
word1 = "abc"
word2 = "pqr"
print(sol.mergeAlternately(word1, word2)) # Output: "apbqcr"