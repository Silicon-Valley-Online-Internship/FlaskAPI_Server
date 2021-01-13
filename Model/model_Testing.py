from tensorflow.keras.models import model_from_json
from PIL import Image, ImageOps
import numpy as np

def prepare_image():
    img = Image.open("applepie_test.jpg")
    img = img.convert("RGB")
    img = img.resize((64,64))

    return img

if __name__=="__main__":
    data = np.ndarray(shape=(1, 64, 64, 3), dtype=np.float32)
    image = Image.open('macarons.jpg')
    size = (64, 64)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    with open("model_arc_10.json", "r") as fp:
        model = model_from_json(fp.read())
    model.load_weights("model_weight_10.h5")

    preds = model.predict(data)
    print(preds)
    print(np.argmax(preds))
