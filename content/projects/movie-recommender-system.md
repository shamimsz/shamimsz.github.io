---
title: "Movie Recommender System with Temporal Evaluation"
summary: "A research-oriented MovieLens 100k recommender system comparing popularity, KNN, and SVD under time-based validation."
order: 1
featured: true
year: "2026"
status: "Completed"
area: "Machine Learning"
tools:
  - Python
  - pandas
  - scikit-surprise
  - MLflow
  - FastAPI
  - Streamlit
  - Docker
  - pytest
links:
  github: "https://github.com/your-github/movie-recommender-system"
  demo: ""
metrics:
  - label: "Dataset"
    value: "MovieLens 100k"
  - label: "Validation"
    value: "Temporal"
  - label: "Best RMSE"
    value: "1.0485"
---

## Problem

Recommendation systems are often evaluated with random splits, but that can
hide look-ahead bias. In a real setting, a model should train on past behavior
and be evaluated on future interactions. I wanted to build a recommender system
that treated evaluation as a serious part of the project, not an afterthought.

## Approach

I used MovieLens 100k and compared a popularity/global-mean baseline,
KNNWithMeans collaborative filtering, and SVD matrix factorization. The main
evaluation used five-fold expanding-window temporal validation, where each
fold trains on earlier ratings and tests on later ratings.

The project measured both rating prediction quality and top-k recommendation
quality. This was important because a model with better RMSE does not
automatically produce better ranked recommendation lists.

## Results

SVD achieved the best rating prediction performance, reducing RMSE by 7.4% and
MAE by 12.5% compared with the popularity/global-mean baseline. However, the
popularity model remained stronger on offline top-k ranking metrics such as
precision@10, recall@10, and nDCG@10.

This result became the main research insight of the project: recommender systems
should be evaluated with both prediction metrics and ranking metrics, because
they answer different questions.

## Implementation Notes

- Implemented temporal splits, RMSE, MAE, precision@10, recall@10, nDCG@10, and
  catalog coverage@10.
- Added seen-item exclusion so users are not recommended movies they already
  rated.
- Added cold-start handling with a popularity fallback for unknown users.
- Served the final SVD model through a FastAPI API with metadata, latency, and
  fallback information.
- Built a Streamlit interface for user history, recommendations, fallback
  status, and model-comparison results.
- Logged experiment results with MLflow and generated reproducible CSV reports.
- Added tests for temporal ordering, top-k metrics, fallback behavior, and API
  responses.

## What I Learned

This project strengthened my interest in recommender systems and careful model
evaluation. The most useful lesson was that a lower prediction error is not the
same as a better user-facing recommendation list.
