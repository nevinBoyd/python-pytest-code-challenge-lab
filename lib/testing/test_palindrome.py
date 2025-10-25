import pytest
from palindrome import longest_palindromic_substring


@pytest.mark.parametrize(
    "input_s, expected_set",
    [
        ("babad", {"bab", "aba"}),             # middle palindrome
        ("cbbd", {"bb"}),                      # even-length palindrome
        ("a", {"a"}),                          # single-character
        ("ac", {"a", "c"}),                    # either char valid
        ("racecar", {"racecar"}),              # entire string palindrome
        ("", {""}),                            # empty string
        ("aaaa", {"aaaa"}),                    # all identical chars
        ("abcdedcbaabcdedcba", {"abcdedcbaabcdedcba"}),  # long palindrome
        ("xyz", {"x", "y", "z"}),              # no multi-char palindrome
    ],
)
def test_longest_palindromic_substring_valid_cases(input_s, expected_set):
    """Check common and edge valid palindrome cases"""
    result = longest_palindromic_substring(input_s)
    assert result in expected_set
    assert result == result[::-1]


def test_non_string_input_raises_typeerror():
    """Ensure function rejects non-string input"""
    with pytest.raises(TypeError):
        longest_palindromic_substring(12345)
