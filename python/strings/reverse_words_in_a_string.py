# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        # Created the response array
        response = []
        # Split the string by spaces and iterate over each word
        for word in s.split(" "):
            # Initialize the variable that will store the reversed word
            reverse = ""
            # Iterate over the word
            for char in word:
                # Add the current character before the existing reversed word
                reverse = char + reverse
            # Add the reversed word to the response list
            response.append(reverse)
        # Join all words in the response list with spaces
        return " ".join(response)
