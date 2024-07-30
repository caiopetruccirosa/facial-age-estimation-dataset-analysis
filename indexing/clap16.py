import pandas as pd

from pathlib import Path

CLAP16_DIR = '/datasets/clap16/appa-real-release'
CLAP16_CSV_PATH = '/datasets/clap16/appa-real-release/data.csv'

def main():
    train_df = pd.read_csv(CLAP16_DIR + '/gt_train.csv')
    val_df = pd.read_csv(CLAP16_DIR + '/gt_valid.csv')
    test_df = pd.read_csv(CLAP16_DIR + '/gt_test.csv')

    train_df['split'] = 'train'
    val_df['split'] = 'validation'
    test_df['split'] = 'test'

    train_df['file_name'] = train_df['file_name'].apply(lambda fn: f'./train/{fn}')
    val_df['file_name'] = val_df['file_name'].apply(lambda fn: f'./valid/{fn}')
    test_df['file_name'] = test_df['file_name'].apply(lambda fn: f'./test/{fn}')

    df = pd.concat([train_df, val_df, test_df], ignore_index=True)

    df.to_csv(CLAP16_CSV_PATH, index=False)

if __name__ == '__main__':
    main()