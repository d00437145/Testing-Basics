import unittest
from challenge import is_palindrome


class TestIsPalindrome(unittest.TestCase):

    def test_simple_palindrome(self):
        """1. Basic lowercase single-word palindrome."""
        self.assertTrue(is_palindrome("racecar"))

    def test_case_insensitivity(self):
        """2. Palindrome with mixed uppercase and lowercase letters."""
        self.assertTrue(is_palindrome("RaceCar"))

    def test_ignores_spaces_and_punctuation(self):
        """3. Sentence palindrome containing spaces and punctuation."""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama!"))

    def test_non_palindrome(self):
        """4. Standard word that is not a palindrome."""
        self.assertFalse(is_palindrome("hello"))

    def test_single_character(self):
        """5. Single character string (trivially a palindrome)."""
        self.assertTrue(is_palindrome("a"))

    def test_empty_string(self):
        """6. Empty string edge case."""
        self.assertTrue(is_palindrome(""))

    def test_numeric_palindrome_string(self):
        """7. String containing digits forming a palindrome."""
        self.assertTrue(is_palindrome("12321"))

    def test_almost_palindrome(self):
        """8. String that differs by only one character at the end."""
        self.assertFalse(is_palindrome("abcb"))

    def test_invalid_input_type(self):
        """9. Non-string input should raise a TypeError."""
        with self.assertRaises(TypeError):
            is_palindrome(12321)


if __name__ == "__main__":
    unittest.main()