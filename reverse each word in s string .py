there are two approaches 
1.split and reverse
2.two pointer approach 
========================================================================================================+++++++++++=========================================
  Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 code:
-------------------------------------------------------------------------------------------
class Solution:
    def reverseWords(self, s: str) -> str:
        l=[]
        s=s.split()
        s=s[::-1]
        return " ".join(s)
-----------------------------------------------
class Solution:
    def reverseWords(self, s: str) -> str:
        i=0
        s=s.split()
        j=len(s)-1
        while i<j :
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return " ".join(s)
