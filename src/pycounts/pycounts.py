from collections import Counter
from string import punctuation


def load_text(input_file):
    """Load text from a text file and return a string.

    Reads from a text file into memory and converts its content to a 
    single string.

    Paramters
    ---------
    input_file : str
        Path to text file.

    Returns
    -------
    str
        Text file contents.

    Examples
    --------
    >>> load_text("test.txt")
    """
    with open(input_file, 'r') as file:
        text = file.read()
    return text


def clean_text(text):
    """Lowercase and remove punctuation from a string.

    Converts a string into lowercase and then removes any punctuation 
    using the built-in punctuation constant of the string class.

    Parameters
    ----------
    text : str
        Text to be made in lowercase and all punctuations removed.

    Returns
    -------
    str
        A text string in lowercase without any punctuation.

    Examples
    --------
    >>> clean_text("Hello World...!")
    'hello world'
    """
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text


def count_words(input_file):
    """Count unique words in a string.

    Words are made lowercase and punctuations are removed
    before counting.

    Parameters
    ----------
    input_file : str
        Path to text file.

    Returns
    -------
    collections.Counter
        dict-like object where keys are words and values are counts.

    Examples
    --------
    >>> count_words("test.txt")
    """
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)
