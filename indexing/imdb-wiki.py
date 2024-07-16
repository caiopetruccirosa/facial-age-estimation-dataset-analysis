import pandas as pd
import numpy as np
import scipy.io as spio

from datetime import datetime, timedelta


# got from https://gist.github.com/victorkristof/b9d794fe1ed12e708b9d
def datenum_to_datetime(datenum):
    """
    Convert Matlab datenum into Python datetime.

    :param datenum: Date in datenum format
    :return:        Datetime object corresponding to datenum.
    """
    days = datenum % 1
    hours = days % 1 * 24
    minutes = hours % 1 * 60
    seconds = minutes % 1 * 60
    return datetime.fromordinal(int(datenum)) \
           + timedelta(days=int(days)) \
           + timedelta(hours=int(hours)) \
           + timedelta(minutes=int(minutes)) \
           + timedelta(seconds=round(seconds)) \
           - timedelta(days=366)

imdb_matdata = spio.loadmat('../datasets/imdb-wiki/imdb_meta/imdb/imdb.mat')
wiki_matdata = spio.loadmat('../datasets/imdb-wiki/wiki/wiki.mat')

# Information got from IMDB-WIKI homepage

# Dataset Features:
#   dob: date of birth (Matlab serial date number)
#   photo_taken: year when the photo was taken
#   full_path: path to file
#   gender: 0 for female and 1 for male, NaN if unknown
#   name: name of the celebrity
#   face_location: location of the face. To crop the face in Matlab run
#   img(face_location(2):face_location(4),face_location(1):face_location(3),:))
#   face_score: detector score (the higher the better). Inf implies that no face was found in the image and the face_location then just returns the entire image
#   second_face_score: detector score of the face with the second highest score. This is useful to ignore images with more than one face. second_face_score is NaN if no second face was detected.
#   celeb_names (IMDB only): list of all celebrity names
#   celeb_id (IMDB only): index of celebrity name
#
# The age of a person can be calculated based on the date of birth and 
# the time when the photo was taken (note that we assume that the photo was 
# taken in the middle of the year):
#   [age,~]=datevec(datenum(wiki.photo_taken,7,1)-wiki.dob); 

attributes_names_idx = {
    'dob': 0,
    'photo_taken': 1,
    'full_path': 2,
    'gender': 3,
    'name': 4,
    'face_location': 5,
    'face_score': 6,
    'second_face_score': 7,
    'celeb_names': 8,
    'celeb_id': 9,
}

wanted_attributes_names = [
    'dob',
    'photo_taken',
    'full_path',
    'gender',
    'name',
]

wanted_attributes_transform = {
    'dob': lambda x: int(datetime.fromordinal(int(x)-366).strftime('%Y')),
    'photo_taken': lambda x: int(x),
    'full_path': lambda x: x[0],
    'gender': lambda x: 'M' if x == 1.0 else 'F' if x == 0.0 else 'U',
    'name': lambda x: x[0] if len(x) > 0 else '[UNKNOWN]',
}

imdb_extracted_data = []

for i in range(len(imdb_np_data[0][0][0][0])):
    data = dict()
    try:
        for att_name in wanted_attributes_names:
            att_idx = attributes_names_idx[att_name]
            raw_data = imdb_np_data[0][0][att_idx][0][i]
            data[att_name] = wanted_attributes_transform[att_name](raw_data)
        data['age'] = data['photo_taken'] - data['dob']
        imdb_extracted_data.append(data)    
    except Exception as e:
        print(f'Error when processing attribute {att_name} with value {raw_data}. Error: {e}')

wiki_extracted_data = []

for i in range(len(wiki_np_data[0][0][0][0])):
    data = dict()
    try:
        for att_name in wanted_attributes_names:
            att_idx = attributes_names_idx[att_name]
            raw_data = wiki_np_data[0][0][att_idx][0][i]
            data[att_name] = wanted_attributes_transform[att_name](raw_data)
        data['age'] = data['photo_taken'] - data['dob']
        wiki_extracted_data.append(data)    
    except Exception as e:
        print(f'Error when processing attribute {att_name} with value {raw_data}. Error: {e}')

df = pd.DataFrame(imdb_extracted_data + wiki_extracted_data)
df.to_csv('../datasets/imdb-wiki/imdb-wiki.csv', index=False)