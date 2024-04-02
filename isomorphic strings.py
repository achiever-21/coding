Time complexity:O(n)
space complexity:O(2000)
'''wo strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
'''
Class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a=[0]*2000
        b=[0]*2000
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if a[ord(s[i])]!=b[ord(t[i])]:
                return False 
            a[ord(s[i])]=i+1
            b[ord(t[i])]=i+1 
        return True
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        map2 = {}
        for i in range(len(s)):
            if s[i] in map:
                if map[s[i]] != t[i]:
                    return False
            if t[i] in map2:
                if map2[t[i]] != s[i]:
                    return False
            else:
                map[s[i]] = t[i]
                map2[t[i]] = s[i]
        return True
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l=[]
        l1=[]
        for i in range(len(s)):
            l.append(s.index(s[i]))
        for i in range(len(t)):
            l1.append(t.index(t[i]))
        if l==l1:
            return True 
        else:
            return False
       
