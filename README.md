# AWS-Based Implicit Recommendation System

This project implements an **implicit-feedback recommendation system** using the Amazon Electronics Reviews dataset.
The system is built end-to-end, from raw data preprocessing to model training and evaluation, and is designed to be
deployable on AWS cloud infrastructure.

---

## Project Overview

- Dataset: Amazon Electronics Reviews
- Feedback Type: Implicit (user–item interactions via reviews)
- Model: Alternating Least Squares (ALS)
- Baseline: Popularity-based recommender
- Cloud: AWS (EC2 / S3 planned)

---

## Problem Statement

Given user interaction data (product reviews), build a recommender system that suggests relevant products to users
based on collaborative filtering.

---

## Project Structure

```text
aws-implicit-recommender/
│
├── src/
│   ├── preprocessing.py        # Convert raw JSON reviews to interactions
│   ├── encode_matrix.py        # Encode users/items and build sparse matrix
│   └── train_als.py             # Train ALS model and generate recommendations
│
├── data/
│   ├── raw/                     # Raw dataset (ignored in Git)
│   └── processed/               # Processed data (ignored in Git)
│
├── models/                      # Trained models (ignored in Git)
├── README.md
└── .gitignore

---

## Parse raw Amazon review JSON

- Extract user–item interactions
- Encode users and items as integer IDs
- Construct a sparse interaction matrix
- Train ALS model on implicit feedback

---
## Evaluation

Metric: Recall@K
Baseline: Popularity-based recommender
Goal: Compare ALS performance against baseline

---
## Tech Stack

- Python
- Pandas, NumPy
- SciPy (Sparse Matrices)
- implicit (ALS)
- Git / GitHub
- AWS (EC2, S3 – upcoming)

---
## Notes

- Raw datasets are not included due to size constraints
- Verified purchases are treated as higher-confidence interactions
- Absence of interaction is treated as unknown (implicit feedback assumption)

---

## Future Improvements

- Time-based train/test split
- Hyperparameter tuning
- Model persistence
- AWS deployment (EC2 + S3)
- API for online recommendations
