# facial-age-estimation-dataset-analysis

A repository containing an analysis of facial images datasets with age annotation:

| **Dataset** | **Download link** |
|---|---|
| AgeDB | *https://www.kaggle.com/datasets/nitingandhi/agedb-database (non-official version)* |
| CACD | *https://bcsiriuschen.github.io/CARC/* |
| CLAP16 | *https://chalearnlap.cvc.uab.cat/dataset/26/description/* |
| FairFace | *https://github.com/joojs/fairface* |
| FG-NET | *https://yanweifu.github.io/FG_NET_data/* |
| IMDB-Clean | *https://github.com/yiminglin-ai/imdb-clean* |
| IMDB-WIKI | *https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/* |
| MORPH | *private link provided* |
| UTKFace | *https://susanqq.github.io/UTKFace/* |

## Running the development environment

The development environment is executed inside a Docker container. The Docker image is described on `./Dockerfile` and the scripts for building the image and running the container are kept on `/scripts`.

## Repository organization

This repository contains the following folders with its domains:

- `/analysis`: contains the notebooks with analysis of each dataset covered.

- `/data`: contains the CSV annotations for all datasets (except MORPH II due to its private nature).

- `/to_csv`: contains the code that extract CSV files of annotations for all datasets and that creates the `/data` folder, based on the datasets storaged as described in [this section](#dataset-storage-structure);

## Dataset storage structure

The directory structure used to store all datasets is the following:

```
/datasets/facial-age-estimation
├── /cacd
│   └── /CACD2000 (downloaded folder)
├── /clap16
│   └── /appa-real-release (downloaded folder)
├── /fairface
│   └── /fairface-img-margin025-trainval (downloaded folder)
├── /fg-net
│   └── /FGNET (downloaded folder)
├── /imdb-clean (cloned repository)
│   ├── ...
│   ├── /data/imdb
│   └── ...
├── /imdb-wiki
│   ├── /imdb_crop (downloaded folder)
│   └── /wiki_crop (downloaded folder)
├── /morph2
│   ├── CD1 (downloaded folder)
│   └── CD2 (downloaded folder)
├── /unofficial-agedb
│   └── /AgeDB (downloaded folder)
└── /utk-face
    ├── /part1 (downloaded folder)
    ├── /part2 (downloaded folder)
    └── /part3 (downloaded folder)
```