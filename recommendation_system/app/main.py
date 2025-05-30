
from flask import Flask
from app.routes.recommendations import bp as recommendations_bp

app = Flask(__name__)
app.register_blueprint(recommendations_bp)

@app.route("/")
def index():
    return "API is running!"

if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
