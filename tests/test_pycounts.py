from pycounts.pycounts import count_words, load_text, clean_text
from pycounts.plotting import plot_words
from pycounts.datasets import get_flatland
from collections import Counter
import matplotlib
import pytest


@pytest.fixture
def einstein_counts():
    return Counter({'insanity': 1, 'is': 1, 'doing': 1,
                    'the': 1, 'same': 1, 'thing': 1,
                    'over': 2, 'and': 2, 'expecting': 1,
                    'different': 1, 'results': 1})


def test_count_words(einstein_counts):
    """Test word counting from a file."""
    expected = einstein_counts
    actual = count_words("tests/einstein.txt")
    assert actual == expected, "ERROR: Incorrect count!"


def test_plot_words(einstein_counts):
    """Test plotting of word counts."""
    counts = einstein_counts
    fig = plot_words(counts)
    assert isinstance(fig, matplotlib.container.BarContainer), \
        "Wrong plot type"
    assert len(fig.datavalues) == 10, \
        "Incorrect number of bars plotted"


@pytest.mark.parametrize(
    "obj",
    [
        3.141,
        "test.txt",
        ["list", "of", "words"]
    ]
)
def test_lot_words_error(obj):
    """
    Checks that TypeError is raised 
    when the argument is not of type Counter
    """
    with pytest.raises(TypeError):
        plot_words(obj)


def test_integration():
    """Test count_words() and plot_words() workflow."""
    counts = count_words("tests/einstein.txt")
    fig = plot_words(counts)
    assert isinstance(fig, matplotlib.container.BarContainer), \
        "Wrong plot type"
    assert len(fig.datavalues) == 10, \
        "Wrong number of bars plotted"
    assert max(fig.datavalues) == 2, \
        "Highest word count should be 2"


def test_regression():
    """Regression test for Flatland"""
    top_word = count_words(get_flatland()).most_common(1)

    # fixtures obtained from CLI
    assert top_word[0][0] == "the", f"Expected 'the', got {top_word[0][0]}"
    assert top_word[0][1] == 2263, f"Expected 2244, got {top_word[0][1]}"
