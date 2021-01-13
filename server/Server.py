import io
from subprocess import call
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from tensorflow.keras.models import model_from_json
from PIL import Image, ImageOps
import numpy as np
import json

app = Flask(__name__)
model = None

@app.route('/upload')
def renderFile():
    return render_template('upload.html')

# Create = POST
# Read = GET
# Update = PUT
# Delete = DELETE

# 단순 파일 업로드용 api
@app.route('/store')
def Renderfile():
    return render_template('store.html')

@app.route('/simpleUpload', methods = ['GET', 'POST'])
def simpleUploadfile():
    if request.method == 'POST':
        f = request.files['file']
        #단순히 파일 저장에 필요한 기능을 하는 API
        f.save(secure_filename(f.filename))

        return 'The file has been stored!'
#여기서 받아들여진 파일을 매개로 바로 알고리즘을 돌린다면?

@app.route('/fileUpload', methods = ['POST'])
def uploadFile():
    if request.method == 'POST':
        print(request.files)
        if request.files.get("image"):
            File = request.files['image'].read()
            img = Image.open(io.BytesIO(File))
            # 저장할 경로 및 파일명 입력(root dir 하위 upload directory)
            #File.save(secure_filename(File.filename))
            #해당 if문 내부에서 subshell 실행해서 foodetector를 실행시킴
            #call('python3 Predict_model.py %s' % secure_filename(File.filename), shell=True)
            preds = predict(img)
            jsonData = labelingPreds(preds)

            #return 'The Class of filaname = (%s) is determined! ' % secure_filename(File.filename)
            return jsonData
        else:
            return "jpg 형식만 업로드 가능합니다"

# predict 함수
# Input : Image File
# Output : Predict data
# 예측값을 라벨 없이 배열값의 형태로만 전달
def predict(img):
    data = np.ndarray(shape=(1, 64, 64, 3), dtype=np.float32)
    size = (64, 64)
    image = ImageOps.fit(img, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    preds = model.predict(data)

    return preds

# labelingPreds 함수
# Input : predict 함수의 preds 결과
# Output : json_data
# Preds 값을 받아 labeling 한 뒤 json 형식으로 리턴하는 함수
def labelingPreds(preds):
    cat = ["Apple Pie", "Bibimbap", "Chicken", "Donuts", "Gyoza",
           "Macarons", "Pancakes", "Pizza", "Sushi", "Waffles"]
    labelIndex = np.argmax(preds)
    result = {"Predict" : cat[labelIndex]}
    json_data = json.dumps(result)

    return json_data

def loadPredictModel():
    global model
    with open("model/model_arc_10.json", "r") as fp:
        model = model_from_json(fp.read())
    model.load_weights("model/model_weight_10.h5")
    print("Model Loading Complete")

if __name__ == "__main__":
    loadPredictModel()
    app.run(host='0.0.0.0', port=5000, debug=True)