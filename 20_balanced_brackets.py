"""
You're given a string s consisting solely of "(" and ")".
Return whether the parentheses are balanced.

Constraints


Example 1
Input
s = "()"

Output
True

Example 2
Input
s = "()()"

Output
True

Example 3
Input
s = ")("

Output
False

Example 4
Input
s = ""

Output
True

Example 5
Input
s = "((()))"

Output
True
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput
# Workout the solution or the logic before you start coding


def balanced_brackets(sentence):
    c1=0
    c2=0
    if sentence.startswith(')'):
        return False
    for i in range(len(sentence)):
        if (sentence[i]=='('):
            c1=c1+1
        else:
            c2=c2+1
    if c1==c2:
        return True
    else:
        return False



# DO NOT TOUCH THE BELOW CODE
class TestBalancedBrackets(unittest.TestCase):

    def test_01(self):
        self.assertEqual(balanced_brackets("()"), True)

    def test_02(self):
        self.assertEqual(balanced_brackets("()()"), True)

    def test_03(self):
        self.assertEqual(balanced_brackets(")("), False)

    def test_04(self):
        self.assertEqual(balanced_brackets(""), True)

    def test_05(self):
        self.assertEqual(balanced_brackets("((()))"), True)

    def test_06(self):
        self.assertEqual(balanced_brackets("((((())))(()))"), True)

    def test_07(self):
        self.assertEqual(balanced_brackets(
            "(((((((((())))))))))()((((()))))"), True)

    def test_08(self):
        self.assertEqual(balanced_brackets(")))))((((("), False)

    def test_09(self):
        self.assertEqual(balanced_brackets(
            "()()(((((((((()()))))))))))((((()))))"), False)

    def test_10(self):
        self.assertEqual(balanced_brackets(
            "()()()(((())))((()))()()(()())(((((())()()()()()))))"), True)

    def test_11(self):
        self.assertEqual(balanced_brackets(
            "()((((((()()()()()((((((())))))))))(())))()))))))()()(((((()))))))))))))))))))())()))"), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
