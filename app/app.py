from flask import Flask, jsonify, request
from google.cloud import firestore
import uuid

app = Flask(__name__)
db = firestore.Client()

# Sample product list (in real use case, this comes from Firestore)
products = [
    {"id": "p1", "name": "Organic Face Cream", "price": 29.99},
    {"id": "p2", "name": "Vitamin C Serum", "price": 45.50},
    {"id": "p3", "name": "Herbal Cleanser", "price": 19.00},
]

@app.route("/")
def index():
    return jsonify({"message": "Welcome to ShopSphere API"}), 200

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products), 200

@app.route("/order", methods=["POST"])
def place_order():
    data = request.get_json()
    product_id = data.get("product_id")
    customer = data.get("customer")

    if not product_id or not customer:
        return jsonify({"error": "Missing data"}), 400

    order_id = str(uuid.uuid4())
    order = {
        "order_id": order_id,
        "product_id": product_id,
        "customer": customer,
        "status": "received"
    }

    db.collection("orders").document(order_id).set(order)
    return jsonify({"message": "Order placed", "order_id": order_id}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
