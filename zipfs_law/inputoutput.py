import pathlib
from typing import List, Tuple
import pandas as pd


def get_input_files(dir: str) -> List[pathlib.Path]:
    """Find all .txt files in the directory"""
    return list(pathlib.Path(dir).glob("*.txt"))


def create_output_directories(dir: str) -> Tuple[pathlib.Path, pathlib.Path]:
    """Create directories if they don't exist."""
    out_path = pathlib.Path(dir)
    out_path.mkdir(exist_ok=True)
    raw_counts_path = (out_path / "raw_counts")
    raw_counts_path.mkdir(exist_ok=True)

    return out_path, raw_counts_path

def get_csv_filename(path: pathlib.Path, stem: str) -> pathlib.Path:
    return path / ( stem + ".csv")

def write_df(stem: str, df: pd.DataFrame, raw_counts_path: pathlib.Path):
    csv_filename = get_csv_filename(raw_counts_path, stem)
    df.to_csv(csv_filename, index=False)

def write_summary(df: pd.DataFrame, out_path: pathlib.Path):
    (
        df
        .set_index("name")
    ).to_csv(out_path / "summary.csv")
