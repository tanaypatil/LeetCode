class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s=="": return ""
        if s==s[::-1]: return s

        # start removing chars from the end until we find a valid palindrome
        # then, reverse whatever was left at the end and append to the beginning
        for i in range(len(s)-1, -1, -1):
            if(s[:i]==s[:i][::-1]):
                to_add = s[i:][::-1]
                break
        return to_add+s
        