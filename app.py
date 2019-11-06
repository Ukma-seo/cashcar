from flask import request, Flask
import sys

sys.path.insert(0, "../../../")

from training_and_serving.app.helpers import *


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/app/v1/predict", methods=["GET"])
def get_prediction():
    model_type = request.args.get("model")
    model = load_model(model_type)
    features = request.args.get("features")
    features = check_features(features)
    price = predict(model, features)
    return {"predicted_price": price}


@app.route("/app/v1/test", methods=["GET"])
def test_func():
    return {"is_alive": 1}

if __name__ == "__main__":
    app.run()
