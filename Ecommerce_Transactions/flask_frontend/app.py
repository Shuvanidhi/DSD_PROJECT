from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# Backend URL
BACKEND_URL = "http://127.0.0.1:8000/api"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/customers")
def customers():
    response = requests.get(f"{BACKEND_URL}/customers/")
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Unable to fetch customers"}), response.status_code

@app.route("/products")
def products():
    response = requests.get(f"{BACKEND_URL}/products/")
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Unable to fetch products"}), response.status_code

@app.route("/transactions")
def transactions():
    response = requests.get(f"{BACKEND_URL}/transactions/")
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Unable to fetch transactions"}), response.status_code

if __name__ == "__main__":
    app.run(debug=True, port=5000)
