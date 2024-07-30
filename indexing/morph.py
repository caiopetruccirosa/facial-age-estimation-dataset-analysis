import pandas as pd

from pathlib import Path

MORPH2_DIR = '/datasets/morph2'
MORPH2_CSV_PATH = '/datasets/morph2/data.csv'

def main():
    df = pd.read_csv(MORPH2_DIR + '/CD2/MORPH_Album2_comp with height and weight.csv')
    df.to_csv(MORPH2_CSV_PATH, index=False)

if __name__ == '__main__':
    main()