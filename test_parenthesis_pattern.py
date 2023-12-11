import unittest
from identify_parenthesis_pattern import check_pattern


# Unit Test cases
class PatternTestCases(unittest.TestCase):
    def test_valid_pattern(self):
        self.assertEqual(check_pattern("()"), True)
        self.assertEqual(check_pattern("(())"), True)
        self.assertEqual(check_pattern("(())()"), True)
        self.assertEqual(check_pattern("()()(())"), True)
    
    def test_invalid_pattern(self):
        self.assertEqual(check_pattern(")("), False)
        self.assertEqual(check_pattern("()())("), False)
        self.assertEqual(check_pattern(")()("), False)
        self.assertEqual(check_pattern("())()("), False)

    def test_unequal_pattern(self):
        self.assertEqual(check_pattern(")()"), False)
        self.assertEqual(check_pattern("()("), False)

if __name__ == '__main__':
    # Unit test execution
    unittest.main()