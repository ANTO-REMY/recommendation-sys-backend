






## Running the App
```sh
& "C:/Users/X 1 YOGA/AppData/Local/Programs/Python/Python313/python.exe" -m app.main
```
The server will start at `http://127.0.0.1:5001/` by default.



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
