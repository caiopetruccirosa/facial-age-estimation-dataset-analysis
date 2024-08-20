import pandas as pd

from pathlib import Path


AGEDB_DIR = '/datasets/unofficial-agedb/AgeDB'
AGEDB_CSV_PATH = '/datasets/unofficial-agedb/AgeDB/data.csv'


def read_dataset(dataset_dir):
    dataset_path = Path(dataset_dir)
    dataset = []
    for file in dataset_path.glob('**/*'):
        if file.suffix != '.jpg':
            print(f'File with extension different than .jpg. File extension found: {file.suffix}')
        else:
            filename = file.stem
            attributes = filename.split('_')
            data = {
                'person_id': attributes[0],
                'person_name': attributes[1],
                'age': int(attributes[2]),
                'sex': attributes[3],
                'filepath': str(file.relative_to(dataset_path))
            }
            dataset.append(data)
    return dataset

def main():
    dataset_data = read_dataset(AGEDB_DIR)
    df = pd.DataFrame(dataset_data)
    df.to_csv(AGEDB_CSV_PATH, index=False)

if __name__ == '__main__':
    main()