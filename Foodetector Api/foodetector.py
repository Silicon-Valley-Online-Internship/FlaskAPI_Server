import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import json
from collections import OrderedDict
import sys
import os

#전체적인 흐름
#모델 및 딕셔너리 파일 로드 -> 분류 -> 결과파일을 json파일로 출력

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

#json 딕셔너리 객체 생성 및 #모델 로드
labels = OrderedDict()
model = tensorflow.keras.models.load_model('keras_model.h5')

# txt파일에 있는 label들을 1차원 배열의 형태로 저장
txt_array = []
with open('labels.txt', 'r') as temp:
    for i in temp:
        txt_array.append(i.rstrip('\n'))


# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
# 정확히 무슨동작하는지 모르겠음
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

#path_string = os.path.abspath(sys.argv[1])
# 바보 최용석
# 이미지 파일을 위의 data배열의 크기에 맞게 조정하고 가운데 중심으로 주변을 깎기
image = Image.open(os.path.abspath(sys.argv[1])) # 파이썬 실행 시 매개변수로 입력된 파일을 open
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
# 이미지 파일 numpy 배열로 변환
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
data[0] = normalized_image_array

#여기서 모델 추론
prediction = model.predict(data)

#도출된 one hot vector를 배열 형태로 변환
pred_trans = np.asarray(prediction)

#2차원 -> 1차원으로 reshape
pred_trans_1d = pred_trans.reshape(-1, 1)


# 원핫 벡터(1)에 해당하는 index값 구하기
index = 0
for j in pred_trans_1d:
    if j == 1:
        break
    else:
        index += 1

#원핫 벡터의 해당해는 순서의 레이블 결과가 딕셔녀리형의 json으로 들어감
labels["result"] = txt_array[index]
print(json.dumps(labels, ensure_ascii=False, indent="\t"))