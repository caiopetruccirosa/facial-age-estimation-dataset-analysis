# facial-age-estimation-dataset-analysis

A repository containing an analysis of facial images datasets with age annotation:

- AgeDB
- CACD
- CLAP16
- FairFace
- FG-NET
- IMDB-Clean
- IMDB-WIKI
- MORPH
- UTKFace

## Execution

Build:

```
#!/bin/bash

echo "requirements.txt file path: $1"
cp $1 ./tmp_build_requirements.txt

docker build --build-arg REQUIREMENTS_FILE=$1 -t cpsrosa-dev .

rm ./tmp_build_requirements.txt
```

Run:

```
#!/bin/bash

echo "notebooks folder path: $1"
echo "datasets folder path: $2"

exec docker run -p 4321:4321 -v "$1":/workspace/notebooks -v "$2":/workspace/datasets -t cpsrosa-dev
```