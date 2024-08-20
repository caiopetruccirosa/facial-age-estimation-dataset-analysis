import pandas as pd

from pathlib import Path

CACD_DIR = '/datasets/cacd/CACD2000'
CACD_CSV_PATH = '/datasets/cacd/CACD2000/data.csv'

def read_dataset(dataset_dir):
    current_path = Path('.')
    dataset_path = Path(dataset_dir)
    dataset = []
    for file in dataset_path.glob('**/*'):
        if file.suffix != '.jpg':
            print(f'File with extension different than .jpg. File extension found: {file.suffix}')
        else:
            filename = file.stem
            attributes = filename.split('_')
            data = {
                'person_name': '_'.join(attributes[1:-1]),
                'picture_per_person_id': int(attributes[-1]),
                'age': int(attributes[0]),
                'filepath': str(file.relative_to(dataset_path))
            }
            dataset.append(data)
    return dataset

def main():
    dataset_data = read_dataset(CACD_DIR)
    df = pd.DataFrame(dataset_data)
    df.to_csv(CACD_CSV_PATH, index=False)

if __name__ == '__main__':
    main()