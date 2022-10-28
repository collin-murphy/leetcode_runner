import sys

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_reduced = '' 
        for l in s:
            if l.isalnum() is True:
                s_reduced += l
                
        print(s_reduced)
