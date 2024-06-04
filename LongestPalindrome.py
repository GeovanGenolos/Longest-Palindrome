from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count the occurences of each character
        char_count = Counter(s)
        length = 0
        odd_found = False

        #iterate through the character counts
        for count in char_count.values():
            # Add the event part of the count to the length
            length += count // 2 * 2
            #check if there is any odd count
            if count % 2 == 1:
                odd_found = True

        # If an odd character count was found, we can place exactly one odd character in the middle
        if odd_found:
            length += 1

        return length
    
sol = Solution()
print(sol.longestPalindrome("abccccdd"))
print(sol.longestPalindrome("a"))