import pandas as pd

from pathlib import Path

FAIRFACE_DIR = '/datasets/fairface/fairface-img-margin025-trainval'
FAIRFACE_CSV_PATH = '/datasets/fairface/fairface-img-margin025-trainval/data.csv'

age_idx_mapping = {
    '0-2': '00-02',
    '3-9': '03-09',
    '10-19': '10-19',
    '20-29': '20-29',
    '30-39': '30-39',
    '40-49': '40-49',
    '50-59': '50-59',
    '60-69': '60-69',
    'more than 70': '70+',
}

def main():
    train_df = pd.read_csv(FAIRFACE_DIR + '/fairface_label_train.csv')
    val_df = pd.read_csv(FAIRFACE_DIR + '/fairface_label_val.csv')

    train_df['split'] = 'train'
    val_df['split'] = 'validation'

    df = pd.concat([train_df, val_df], ignore_index=True)

    # create new age column
    df['raw_age'] = df['age']

    df['age'] = df['raw_age'].apply(lambda row_data: age_idx_mapping[row_data])

    df.to_csv(FAIRFACE_CSV_PATH, index=False)

if __name__ == '__main__':
    main()