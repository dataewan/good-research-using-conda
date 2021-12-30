from io import TextIOWrapper
import string
import collections
from typing import Dict
import pandas as pd


def _clean_guttenberg(text: str) -> str:
    start_fence = "start of the project gutenberg ebook"
    end_fence = "end of the project gutenberg ebook"
    text = text.lower()
    start_pos = text.find(start_fence) + len(start_fence) + 1
    end_pos = text.find(end_fence)
    return text[start_pos:end_pos]


def count_words(fname: TextIOWrapper, clean_text: bool = False) -> Dict[str, int]:
    """Count the words in a text file

    fname:
        File to count words in

    clean_text:
        Should we remove the guttenberg header and footer?
    """

    text = fname.read()

    if clean_text:
        text = _clean_guttenberg(text)

    chunks = text.split()
    npunc = [word.strip(string.punctuation) for word in chunks]
    word_list = [word.lower() for word in npunc if word]
    word_counts = collections.Counter(word_list)
    return dict(word_counts)


def word_counts_to_df(word_counts: Dict[str, int]) -> pd.DataFrame:
    df = pd.DataFrame({"word": x, "freq": y} for x, y in word_counts.items())

    return df.sort_values("freq", ascending=False)
