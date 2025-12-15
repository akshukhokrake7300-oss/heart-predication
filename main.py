from flask import Flask, jsonify, request,render_template
import pandas as pd
import config
import pymongo
from src.database import Obj


from artifacts import encoded_target


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")


# ------------ Load Dataset Once ------------
df = pd.read_csv(r"C:\Users\akshu\heart.csv")   # your CSV file name
target_values = list(df['target'].unique())

# ------------ Target API -------------------
@app.route("/target", methods=["GET"])
def target():
    return jsonify({
        "unique_target_values": target_values

    })
@app.route("/target_page")
def target_page():
    return render_template("target.html", targets=target_values)
# ------------ Prediction API ---------------
@app.route("/predict", methods=["POST"])
def predict():

    # 1) Input JSON
    data = request.json

    try:
        input_data = [
            data["age"],
            data["gender"],
            data["cp"],
            data["trestbps"],
            data["chol"],
            data["fbs"],
            data["restecg"],
            data["thalach"],
            data["exang"],
            data["oldpeak"],
            data["slope"],
            data["ca"],
            data["thal"]
        ]
    except:
        return jsonify({"error": "Missing input keys!"}), 400

    # 2) Load ML model
    model = Obj.load_model()

    # 3) Prediction
    pred = model.predict([input_data])[0]  # 0 or 1

    # 4) Decode prediction label
    label = decode.get(pred, "unknown")

    return jsonify({
        "prediction": int(pred),
        "label": label
    })
@app.route("/predict_page")
def predict_page():
    return render_template("predict.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.FLASK_PORT_NUMBER, debug=True)

