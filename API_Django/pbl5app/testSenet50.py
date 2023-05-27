from tensorflow.keras.models import load_model
# returns a compiled model identical to the previous one
model = load_model('senet50_transfer_learning_trained_face_cnn_model.h5')

import cv2
import os
import pickle
import numpy as np
import pickle

from PIL import Image
from keras.preprocessing import image
from keras_vggface import utils
import pandas as pd

# dimension of images
image_width = 224
image_height = 224

# chạy feature extraction trên tập huấn luyện
import tensorflow as tf
import face_recognition
import os

encodeListKnow = []
classnames = []
dem = 0
folder_path = f'./HuanLuyen'

for root, dirs, files in os.walk(folder_path):
    name = root.split("/")[-1]
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg") or True:

            test_image_filename = os.path.join(root, file)
            namecorrect = file.split(" ")[0]

            imagetest = face_recognition.load_image_file(test_image_filename)
            imagetest = cv2.cvtColor(imagetest, cv2.COLOR_BGR2RGB)

            # detect face
            faces = face_recognition.face_locations(imagetest)

            # if not exactly 1 face is detected, skip this photo
            if len(faces) == 0:
                print(f'---We need exactly 1 face; photo skipped---')
                continue
            dem += 1
            print(dem)
            for (y1, x2, y2, x1) in faces:
                # resize the detected face to 224x224
                size = (image_width, image_height)

                # detected face region
                roi = imagetest[y1:y2, x1:x2]

                # resize the detected head to target size
                resized_image = cv2.resize(roi, size)

                # prepare the image for prediction
                x = tf.keras.preprocessing.image.img_to_array(resized_image)
                x = np.expand_dims(x, axis=0)
                x = utils.preprocess_input(x, version=1)

                # making prediction
                predicted_prob = model.predict(x)
                print(predicted_prob)
                # print(predicted_prob[0].argmax())
                encode = predicted_prob[0]
                encodeListKnow.append(encode)
                classnames.append(name)
            print("------------------------------------------------------------------------------\n")

# save encodeListKnow + classnames in file know_face_encode.csv
# Create a DataFrame to store the face encodings
df = pd.DataFrame(encodeListKnow)
dfname = pd.DataFrame(classnames)

print(df)
print(dfname)

# # Save the DataFrame to a CSV file
# df.to_csv("/content/drive/MyDrive/Colab Notebooks/keras-vggface/SaveDir/know_face_encode.csv", index=False)
# dfname.to_csv("/content/drive/MyDrive/Colab Notebooks/keras-vggface/SaveDir/know_face_classnames.csv", index=False)


def MaHoaSeNet50(images):
    list_encodes = []
    for image in images:
        imagetest = cv2.cvtColor(imagetest, cv2.COLOR_BGR2RGB)
        # detect face
        faces = face_recognition.face_locations(imagetest)
        # if not exactly 1 face is detected, skip this photo
        if len(faces) == 0:
            print(f'---We need exactly 1 face; photo skipped---')
            continue
        for (y1, x2, y2, x1) in faces:
            # resize the detected face to 224x224
            size = (image_width, image_height)
            # detected face region
            roi = imagetest[y1:y2, x1:x2]
            # resize the detected head to target size
            resized_image = cv2.resize(roi, size)
            # prepare the image for prediction
            x = tf.keras.preprocessing.image.img_to_array(resized_image)
            x = np.expand_dims(x, axis=0)
            x = utils.preprocess_input(x, version=1)
            # making prediction
            predicted_prob = model.predict(x)
            print(predicted_prob)
            # print(predicted_prob[0].argmax())
            encode = predicted_prob[0]
            list_encodes.append(encode)
    return list_encodes
def EncodeFrameSenet50(image):
    list_encode = []
    imagetest = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # detect face
    faces = face_recognition.face_locations(imagetest)
    # if not exactly 1 face is detected, skip this photo
    if len(faces) == 0:
        print(f'---We need exactly 1 face; photo skipped---')
        return list_encode
    for (y1, x2, y2, x1) in faces:
        # resize the detected face to 224x224
        size = (image_width, image_height)
        # detected face region
        roi = imagetest[y1:y2, x1:x2]
        # resize the detected head to target size
        resized_image = cv2.resize(roi, size)
        # prepare the image for prediction
        x = tf.keras.preprocessing.image.img_to_array(resized_image)
        x = np.expand_dims(x, axis=0)
        x = utils.preprocess_input(x, version=1)
        # making prediction
        predicted_prob = model.predict(x)
        print(predicted_prob)
        # print(predicted_prob[0].argmax())
        encode = predicted_prob[0]
        list_encode.append(encode)
    return list_encode