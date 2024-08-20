import pandas as pd

from pathlib import Path

IMDB_CLEAN_DIR = '/datasets/imdb-clean/csvs'
IMDB_CLEAN_CSV_PATH = '/datasets/imdb-clean/data.csv'

def main():
    train_df = pd.read_csv(IMDB_CLEAN_DIR + '/imdb_train_new.csv')
    val_df = pd.read_csv(IMDB_CLEAN_DIR + '/imdb_valid_new.csv')
    test_df = pd.read_csv(IMDB_CLEAN_DIR + '/imdb_test_new.csv')

    train_df['split'] = 'train'
    val_df['split'] = 'validation'
    test_df['split'] = 'test'

    df = pd.concat([train_df, val_df, test_df], ignore_index=True)
    df['filename'] = df['filename'].apply(lambda fn: f'./data/imdb/{fn}')

    df.to_csv(IMDB_CLEAN_CSV_PATH, index=False)

if __name__ == '__main__':
    main()