In this assignment, you should write your code in a **readable** way.

Your function definitions should have **appropriate docstrings**.

# Assignment 8: Recursion

## Part 1: Reversing

Write a recursive function, `reverse(text)`, that reverses a given string `text` as follows:

1. Take the first character,
2. Call `reverse()` with the rest of the string,
3. And append the first character (from Step 1) to the result from Step 2.

Implement the `reverse()` function.

**Hint:** Recall the three conditions for successful recursion. Check that your `reverse()` function fulfills all three conditions.

## Part 2: Palindromes

A palindrome is a sentence or number with a sequence of letters, such that it reads the same way forwards and backwards.

Write a recursive function, `is_palindrome()`, that takes in an input string and checks whether it is a valid palindrome.

1. The result should be case-insensitive.
2. The function should ignore punctuation and whitespace.
3. The function should return `True` if the string is a valid palindrome, and `False` otherwise.

**Hint 1:** A palindrome should have the first and last letters be the same.

**Hint 2:** If a string has more than two letters is a valid palindrome and, the same string without its first and last letters is also a palindrome.

(optional) Add `print()` statements to generate a trace table that you can use to check if `is_palindrome()` is carrying out its operations correctly.

# Submission

Before submitting your code, run the automated tests on your functions. In the shell, type `python test_main.py` and press enter to see the results of the testing.

