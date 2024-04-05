# Built-in imports

def reverse(text):
    """
    reverses given text
    ---------
    string text:
        text
    --------
    string bword:
        word but first letter is now behind
    """
    if len(text) == 0: 
        return ''
    if len(text) == 1:
        return text
    else:
        return text[-1] + reverse(text[:-1]) 

def is_palindrome(word):
    """
    outputs whether a word is a palindrome
    ---------
    string word
        word
    ------------
    boolean truth
        whether the inputed text is a palindrome
    """
    if len(word) == 0:
        return True
    if len(word) == 1:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1]) 
    else:
        return False
