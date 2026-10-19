
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to our Retail Loyalty Platform!",
        "status": "running"
    })


@app.route("/loyalty")
def loyalty():
    return jsonify({
        "customer": "Anjali",
        "loyalty_points": 250,
        "message": "Your loyalty points are available!"
    })


@app.route("/promotions")
def promotions():
    return jsonify({
        "promotions": [
            {
                "id": 1,
                "title": "Summer Sale",
                "discount": "10%"
            },
            {
                "id": 2,
                "title": "Loyalty Member Offer",
                "discount": "15%"
            }
        ]
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
