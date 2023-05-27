import cv2
import os
import face_recognition
import pandas as pd
import numpy as np
import tensorflow as tf
from keras_vggface import utils
from tensorflow.keras.models import load_model

resize = 300
def Mahoa (images):
    list_encodes = []
    for image in images:
        framS = cv2.resize(image, (0, 0), None, fx=0.5, fy=0.5)
        framS = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encodes = face_recognition.face_encodings(framS)
        for encode in encodes:
            list_encodes.append(encode)
    return list_encodes

def MaHoaSeNet50(images):
    # returns a compiled model identical to the previous one
    model = load_model('senet50_transfer_learning_trained_face_cnn_model.h5')
    list_encodes = []
    for image in images:
        imagetest = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # detect face
        faces = face_recognition.face_locations(imagetest)
        # if not exactly 1 face is detected, skip this photo
        if len(faces) == 0:
            print(f'---We need exactly 1 face; photo skipped---')
            continue
        for (y1, x2, y2, x1) in faces:
            # resize the detected face to 224x224
            size = (224, 224)
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

def ListEncodeVideo(cap):

    # print(f"Thời gian của video là: {duration_sec} giây")
    times = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]

    # Tạo thư mục folder1 nếu nó không tồn tại
    if not os.path.exists('folder1'):
        os.makedirs('folder1')

    images = []
    # Lặp qua các thời điểm và cắt ảnh
    for i, t in enumerate(times):
        # Đặt chỉ số khung hình
        frame_idx = int(t * cap.get(cv2.CAP_PROP_FPS))
        # Đặt con trỏ đến khung hình cần cắt
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        # Đọc khung hình
        ret, frame = cap.read() 
        
        cv2.imwrite(f'folder1/frame{i}.jpg', frame)
        images.append(frame) 

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return MaHoaSeNet50(images)

if __name__ == "__main__":
    # Đường dẫn đến video của bạn
    video_path = r'C:\Users\ACER\PycharmProjects\AnacondaFace\git\PBL5\Source Backend\mysite\static\videos\Cuong.mp4'
    # Load video
    cap = cv2.VideoCapture(video_path)
    # lấy danh sách encode từ video
    list_encodes = ListEncodeVideo(cap)
    # lưu encode vào file
    df = pd.DataFrame(list_encodes)
    df.to_csv("AnacondaFace/system/SaveDir/list_encodes_client.csv", index=False)