"""
Given an integer x, return true if x is a palindrome
integer (LeetCode #9)
"""

def palindromeNumber(x: int) -> bool:
    str_num = str(x)
    start = 0
    end = len(str_num) - 1
    
    while start < end:
        if str_num[start] == str_num[end]:
            start += 1
            end -= 1
        else:
            return False
        
    return True

print(palindromeNumber(22322))