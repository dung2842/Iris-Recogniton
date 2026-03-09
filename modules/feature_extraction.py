import cv2
import numpy as np
from tensorflow.keras.models import load_model, Model

# load model
model = load_model("model/IRISRecognizer.h5")

# tạo feature extractor
feature_model = Model(
    inputs=model.inputs,
    outputs=model.layers[-2].output
)

def extract_feature(image_path):

    img = cv2.imread(image_path, 0)

    # resize đúng kích thước model
    img = cv2.resize(img, (64,64))

    img = img / 255.0
    img = img.reshape(1,64,64,1)

    feature = feature_model.predict(img)

    return feature[0]