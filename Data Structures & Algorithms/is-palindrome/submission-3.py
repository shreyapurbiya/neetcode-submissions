class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace(" ","")
        palindrome=[]
        for letter in s:
            if letter.isalnum():
                palindrome.append(letter)
        print(palindrome)
        if palindrome== palindrome[::-1]:
            return True
        else:
            return False 

