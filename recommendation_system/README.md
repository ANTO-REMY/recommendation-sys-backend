

# AI-Powered Recommendation System Backend

This project is a backend service that provides personalized item recommendations to users based on their past interactions. It is built using Python, Flask, Pandas, NumPy, and scikit-learn, and implements collaborative filtering with cosine similarity to generate recommendations.

## What This Application Does

- Provides a REST API for generating personalized recommendations for users.
- Uses collaborative filtering to analyze user-item interaction data and suggest items a user is likely to enjoy.
- Designed for easy integration into larger systems (e.g., e-commerce, content platforms, etc.).

## Tech Stack

- **Python 3.13**
- **Flask** (web framework)
- **Pandas** (data manipulation)
- **NumPy** (numerical operations)
- **scikit-learn** (cosine similarity calculation)

## Use Case

This backend is ideal for any platform that wants to provide personalized recommendations to its users, such as:
- E-commerce sites (product recommendations)
- Streaming services (movie, music, or video recommendations)
- News or content platforms (article suggestions)

## Main Function

Given a user ID, the API analyzes the user's past ratings/interactions and returns a list of recommended item IDs that the user has not yet interacted with, ranked by predicted relevance.

## Features
- Collaborative filtering using user-item interaction data
- Cosine similarity for personalized recommendations
- REST API endpoint for recommendations
- Easy to extend and integrate

## Project Structure

```
recommendation_system/
│
├── app/
│   ├── main.py                  # Flask app entry point
│   ├── models/
│   │   └── recommender.py       # Recommendation logic
│   ├── routes/
│   │   └── recommendations.py   # API endpoint(s)
│   └── data/
│       ├── interactions.csv     # User-item interaction data
│       └── items.csv            # Item metadata (optional)
│
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── .gitignore                   # Files/folders to ignore in version control
```

## Setup
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Add your user-item interaction data to `app/data/interactions.csv` (columns: user_id, item_id, rating).
3. (Optional) Add item metadata to `app/data/items.csv`.


## Running the App
```sh
& "C:/Users/X 1 YOGA/AppData/Local/Programs/Python/Python313/python.exe" -m app.main
```
The server will start at `http://127.0.0.1:5001/` by default.

## API Usage

### Get Recommendations
**Endpoint:** `/recommend`

**Method:** `GET`

**Query Parameters:**
- `user_id` (required): The user ID to get recommendations for.


**Example:**
```
GET http://127.0.0.1:5001/recommend?user_id=1
```


**Response:**
```json
{
  "user_id": 1,
  "recommendations": [104, 103]
}
```

## License
MIT
