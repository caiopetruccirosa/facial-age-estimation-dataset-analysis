import pandas as pd

from datetime import datetime
from pathlib import Path


UTKFACE_DIR = '/datasets/agedb/AgeDB'
UTKFACE_CSV_PATH = '/datasets/agedb/AgeDB/data.csv'
DATASET_DATETIME_FORMAT = '%Y%m%d%H%M%S%f'
READABLE_DATETIME_FORMAT = "%d/%m/%Y %H:%M:%S.%f"
GENDER_MAPPING = {
    '0': 'M',
    '1': 'F',
}
RACE_MAPPING = {
    '0': 'White',
    '1': 'Black',
    '2': 'Asian',
    '3': 'Indian',
    '4': 'Others',
}
FILENAME_EXCEPTIONS = {
    '44_1_4_20170116235150272.pg': '44_1_4_20170116235150272',
    '55_0_0_20170116232725357jpg': '55_0_0_20170116232725357'
}


def read_dataset(dataset_dir):
    current_path = Path('.')
    dataset_path = Path(dataset_dir)
    dataset = []
    files_with_error = []
    for file in dataset_path.glob('**/*'):
        if not file.is_file():
            continue
        if file.name == '.DS_Store':
            continue
        if file.suffix in ['.zip','.gz', '.tar']:
            continue
        if file.name not in FILENAME_EXCEPTIONS.keys() and file.suffix not in ['.jpg','.JPG']:
            print(f'File with extension different than .jpg. Filename: {file}')
            continue
            
        if file.name in FILENAME_EXCEPTIONS.keys():
            filestem = FILENAME_EXCEPTIONS[file.name]
        else:
            filestem = file.stem.strip()
        
        try:
            raw_age, raw_gender, raw_race, raw_datetime = filestem.split('_')
            
            age = int(raw_age)
            gender = GENDER_MAPPING[raw_gender]
            race = RACE_MAPPING[raw_race]
            tmp_dt = datetime.strptime(raw_datetime, DATASET_DATETIME_FORMAT)
            dt = tmp_dt.strftime(READABLE_DATETIME_FORMAT)
        except Exception as e:
            print(f'Error parsing data attributes. Error: {e}')
            files_with_error.append(str(file))
            continue

        data = {
            'age': age,
            'gender': gender,
            'race': race,
            'datetime': dt,
            'filepath': str(file.relative_to(current_path))
        }
        dataset.append(data)
    return dataset, files_with_error


def main():
    dataset_data, files_with_error = read_dataset(UTKFACE_DIR)

    for file_with_error in files_with_error:
        print(file_with_error)

    df = pd.DataFrame(dataset_data)
    df.to_csv(UTKFACE_CSV_PATH, index=False)

if __name__ == '__main__':
    main()