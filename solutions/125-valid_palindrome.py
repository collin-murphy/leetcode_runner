class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_reduced = '' 
        for l in s:
            if l.isalnum() is True:
                s_reduced += l.lower()
               
        head = 0
        tail = len(s_reduced) - 1
        
        while head <= tail:
            if not s_reduced[head] == s_reduced[tail]:
                return False
            head += 1
            tail -= 1


        print(s_reduced)
        return True
