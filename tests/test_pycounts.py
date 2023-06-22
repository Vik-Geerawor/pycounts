from pycounts.pycounts import count_words, load_text, clean_text
from collections import Counter


def test_load_text():
    expected = 'Insanity is doing the same thing over and over and expecting different results.'
    actual = load_text('tests/einstein.txt')
    assert actual == expected, "ERROR: File not loaded correctly!"


def test_clean_text():
    expected = 'insanity is doing the same thing over and over and expecting different results'
    actual = clean_text('Insanity is doing the same thing over and over and expecting different results.')
    assert actual == expected, "ERROR: punctuations not cleared!"


def test_count_words():
    """Test word counting from a file."""
    expected = Counter({'insanity': 1, 'is': 1, 'doing': 1,
                        'the': 1, 'same': 1, 'thing': 1,
                        'over': 2, 'and': 2, 'expecting': 1,
                        'different': 1, 'results': 1})
    actual = count_words("tests/einstein.txt")
    assert actual == expected, "ERROR: Incorrect count!"
