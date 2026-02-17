# MovieLens Implicit ALS Recommender

## Overview
Built an implicit-feedback recommendation system using ALS matrix factorization on MovieLens 20M dataset.

## Architecture
S3 → Colab (training) → ALS → S3 model storage

## Data Processing
- Converted explicit ratings to implicit interactions
- Temporal train/test split
- Encoded user/item IDs
- Built sparse interaction matrix

## Model
- Implicit ALS
- Hyperparameter tuning performed

## Evaluation
Recall@10: 0.09
MAP@10: 0.045

### Diversity Analysis
Average Genre Diversity@10

### Popularity Bias
Average recommendation popularity vs dataset baseline

## Limitations
- Cold-start users/items
- Popularity bias
- Offline evaluation only

## Future Improvements
- Hybrid model
- Real-time API endpoint
- Approximate nearest neighbor search
