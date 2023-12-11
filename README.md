# pattern_match
The code performs pattern matching for a string made of only open and closed simple braces.
If the string is made of properly grouped open and closed braces, return True, else return False.

# Examples:
===========
1. Valid input patterns.
    a) ()
    b) (())
    c) (())()
    d) ()()(())

2. Invalid input patterns.
    a) )(
    b) ())(
    c) ())(()

3) unequal number of braces in pattern
    a) ()(
    b) (()))

Source code: identify_parenthesis_pattern.py
Test Cases: test_parenthesis_pattern.py file
Python Version : 3.11.5