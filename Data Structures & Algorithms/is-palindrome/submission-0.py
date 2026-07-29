class Solution:
    def isPalindrome(self, s: str) -> bool:
        array_s= list(s)
        first= 0
        last= len(s)-1
        while first < last:
            while first < last and not array_s[first].isalnum():
                first +=1

            while first < last and not array_s[last].isalnum():
                last -=1

            if array_s[first].lower() != array_s[last].lower():
                return False
            first +=1
            last -=1  

        return True        
        
        