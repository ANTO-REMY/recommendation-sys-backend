
# Algorithmic(ML) Recommendation System

This project is a backend service that provides personalized item recommendations to users based on their past interactions. It is built using Python, Flask, Pandas, NumPy, and scikit-learn, and implements collaborative filtering with cosine similarity to generate recommendations.

## What This Project Does

- Provides a REST API for generating personalized recommendations for users.
- Uses collaborative filtering to analyze user-item interaction data and suggest items a user is likely to enjoy.
- Designed for easy integration into larger systems (e.g., e-commerce, content platforms, etc.).

## Requirements

See `requirements.txt` for a list of dependencies. Main requirements:

- Python 3.13
- Flask
- Pandas
- NumPy
- scikit-learn

## Use Case

This backend is ideal for any platform that wants to provide personalized recommendations to its users, such as:
- E-commerce sites (product recommendations)
- Streaming services (movie, music, or video recommendations)
- News or content platforms (article suggestions)

## Main Function

Given a user ID, the API analyzes the user's past ratings/interactions and returns a list of recommended item IDs that the user has not yet interacted with, ranked by predicted relevance.

```
The server will start at `http://127.0.0.1:5001/` by default.

### API Endpoint

- Endpoint: `/recommend`
- Method: `GET`
- Query Parameters:
  - `user_id` (required): The user ID to get recommendations for.

Example:

```
```
GET http://127.0.0.1:5001/recommend?user_id=1
```
```
Response:
```json
{
  "user_id": 1,
  "recommendations": [104, 103]
}
```

