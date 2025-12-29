from flask import Flask, request, jsonify
from flask_cors import CORS
from app.utils import predict_message

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/predict", methods=["POST"])
def predict_sms():
    data = request.get_json()

    message = data.get("message")

    if not message:
        return jsonify({"error": "Message is required"}), 400

    pred = predict_message(message)

    return jsonify({
        "message": message,
        "prediction": pred
    })

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "SMS Spam Classifier API Running!"})

if __name__ == "__main__":
    app.run(debug=True)
