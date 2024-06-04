# This is my code in solving LeetCode Longest Palindrome.

'''
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
'''

# Explanation:

-Character Counting: We use the Counter from the collections module to count the occurrences of each character in the string.

-Calculate Length: We initialize length to 0 and odd_found to False. We iterate through the values in char_count:

  -For each character count, we add the largest even number less than or equal to the count to length using count // 2 * 2.

  -If a count is odd, we set odd_found to True.

-Adjust for Odd Character: After the loop, if odd_found is True, it means we can add one odd character in the center of the palindrome, so we increment length by 1.

-Return Result: Finally, we return the computed length.

-This code is efficient with a time complexity of O(n), where n is the length of the input string s, and it uses space proportional to the number of unique characters in s.
