from tensorflow.keras.models import model_from_json
from PIL import Image, ImageOps
import numpy as np
import flask
import io

app = flask.Flask(__name__)
model = None

def prepare_imageData(image):
    data = np.ndarray(shape=(1, 64, 64, 3), dtype=np.float32)
    image = ImageOps.fit(image, (64, 64), Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    return data

def init_model():
    with open("model_arc.json", "r") as fp:
        model = model_from_json(fp.read())
    model.load_weights("model_weight.h5")

@app.route("/predict", methods=["POST"])
def predict():
    data = {"success" : False}

    if flask.request.method == "POST":
        image = flask.request.files["image"].read()
        image = Image.open(io.BytesIO(image))
        image_data = prepare_imageData(image)

        preds = model.predict(image_data)

        data["success"] = True

    return flask.jsonify(data)

def testing():
    str1 = "dddd.jpg"
    str2 = "dddd"

    if(str)

if __name__=="__main__":
    print(("* Loading Keras model and Flask starting server..."
           "please wait until server has fully started"))
    init_model()
    app.run()
