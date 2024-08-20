import pandas as pd

from pathlib import Path

FGNET_DIR = '/datasets/fg-net/FGNET/FGNET/images'
FGNET_CSV_PATH = '/datasets/fg-net/FGNET/data.csv'

def read_dataset(dataset_dir):
    filter_non_numeric = lambda s: ''.join(c for c in s if c.isdigit())
    filter_numeric = lambda s: ''.join(c for c in s if not c.isdigit())

    current_path = Path('.')
    dataset_path = Path(dataset_dir)
    dataset = []
    for file in dataset_path.glob('**/*'):
        if file.suffix not in ['.jpg','.JPG']:
            print(f'File with extension different than .jpg. File extension found: {file.suffix}')
        else:
            filename = file.stem
            attributes = filename.split('A')
            
            raw_person_id = attributes[0]
            raw_age = attributes[1]
            
            photo_id_suffix = 'a' 
            
            if not raw_age.isnumeric():
                raw_age = filter_non_numeric(raw_age)
                photo_id_suffix = filter_numeric(raw_age)
            
            data = {
                'person_id': raw_person_id,
                'photo_id': f'{raw_person_id}{photo_id_suffix}',
                'age': int(raw_age),
                'filepath': str(file.relative_to(dataset_path))
            }
            dataset.append(data)
    return dataset

def main():
    dataset_data = read_dataset(FGNET_DIR)
    df = pd.DataFrame(dataset_data)
    df.to_csv(FGNET_CSV_PATH, index=False)

if __name__ == '__main__':
    main()