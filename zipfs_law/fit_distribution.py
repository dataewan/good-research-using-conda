from typing import Dict, Tuple, Union
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

from dataclasses import dataclass


@dataclass
class SummaryStatistics:
    total_words: int
    distinct_words: int
    alpha: float
    C: float

    def to_dict(self, name: str) -> Dict[str, Union[int, float, str]]:
        return {
            "name": name,
            "total_words": self.total_words,
            "distinct_words": self.distinct_words,
            "alpha": self.alpha,
            "C": self.C
        }


def compute_summary(word_counts: Dict[str, int]) -> SummaryStatistics:
    """
    Compute the summary stats for the distribution of word counts
    """

    wc = np.array(list(word_counts.values()))
    alpha, C = estimate_zipf(wc)

    return SummaryStatistics(
        total_words=wc.sum(),
        distinct_words=len(wc),
        alpha=alpha,
        C=C,
    )


def estimate_zipf(wc: np.ndarray) -> Tuple[float, float]:
    """
    Fit Zipf distribution to a set of word counts.

    Returns:
        Alpha and C for the word count distribution
    """
    mle = minimize_scalar(
        _nlog_likelihood, bracket=(1 + 1e-10, 4), args=wc, method="brent"
    )

    beta = mle.x
    alpha = 1 / (beta - 1)
    C = ((np.arange(len(wc)) + 1) ** (-alpha)).sum()

    return alpha, C


def _nlog_likelihood(beta, counts):
    likelihood = -np.sum(
        np.log((1 / counts) ** (beta - 1) - (1 / (counts + 1)) ** (beta - 1))
    )

    return likelihood
