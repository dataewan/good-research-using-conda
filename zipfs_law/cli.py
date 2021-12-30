import click
import pandas as pd

from . import parse_text, inputoutput, fit_distribution

def run_analysis(in_folder: str, out_folder: str):
    filepaths = inputoutput.get_input_files(in_folder)
    out_path, raw_counts_path = inputoutput.create_output_directories(out_folder)

    summaries = []
    for infilepath in filepaths:
        with open(infilepath, "r") as f:
            word_counts = parse_text.count_words(f, clean_text=True)
            df = parse_text.word_counts_to_df(word_counts)
            inputoutput.write_df(stem=infilepath.stem, df=df, raw_counts_path=raw_counts_path)

            summary = fit_distribution.compute_summary(word_counts)
            summaries.append(summary.to_dict(infilepath.stem))

    inputoutput.write_summary(pd.DataFrame(summaries), out_path)


    


@click.command()
@click.argument("in_folder")
@click.argument("out_folder")
def main(in_folder: str, out_folder: str):
    run_analysis(in_folder, out_folder)
