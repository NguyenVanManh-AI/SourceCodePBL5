# khi upload ảnh khuôn mặt lên hệ thống
# hệ thống sẽ trích xuất đặc trưng của khuôn mặt đó + nhãn của khuôn mặt thêm vào ứng dụng

# đọc ảnh muốn thêm vào dữ liệu
import cv2
import face_recognition
import os
import pandas as pd
import csv


def save_know_face_encode(encode):
    # Hàng mới cần thêm vào
    new_row = encode

    # Mở file CSV trong chế độ "append"
    with open("../../AnacondaFace/system/SaveDir/know_face_encode.csv", 'a', newline='') as file:
        writer = csv.writer(file)

        # Ghi hàng mới vào cuối file
        writer.writerow(new_row)

def save_know_face_classname(name):
    # Hàng mới cần thêm vào
    new_row = [name]

    # Mở file CSV trong chế độ "append"
    with open("../../AnacondaFace/system/SaveDir/know_face_classnames.csv", 'a', newline='') as file:
        writer = csv.writer(file)

        # Ghi hàng mới vào cuối file
        writer.writerow(new_row)

resize = 300
pathTrain = "HuanLuyenNew"
images = []
classnames = []
myList = os.listdir(pathTrain)
print(myList)
for cl in myList:
    print(cl)
    curImg = cv2.imread(f"{pathTrain}/{cl}")
    images.append(curImg)
    str1 = os.path.splitext(cl)[0]
    str1 = str1[:str1.rindex('_')]
    classnames.append(str1)
    #splitext sẽ tách chuỗi ra làm 2 phần tên và phần mở rộng
print(len(images))
print(classnames)

#step encoding
def Mahoa (images):
    encodeList = []
    for img, index in zip(images, range(len(images))):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        locationFace = face_recognition.face_locations(img)
        if len(locationFace) != 0:
            y1, x2, y2, x1 = locationFace[0]
            print(locationFace[0])
            paddingX = int((x2-x1)*0.2)
            paddingY = int((y2-y1)*0.2)
            # Get original height and width
            h, w, c = img.shape
            print("Original Height and Width:", h, "x", w)
            cropped_img = img[max(y1-paddingY,0):min(y2+paddingY, h), max(x1-paddingX,0):min(x2+paddingX, w)]
            down_width = int(resize)
            down_height = int((y2-y1)*resize/(x2-x1))
            down_points = (down_width, down_height)
            resize_down = cv2.resize(cropped_img, down_points, interpolation=cv2.INTER_LINEAR)
            cv2.imwrite(f"cutImage/{myList[index]}", resize_down)
            # Get original height and width
            h1, w1, c1 = resize_down.shape
            print("Original Height and Width:", h1, "x", w1)
            encode = face_recognition.face_encodings(resize_down)
            if len(encode) != 0:
                encode = encode[0]
                encodeList.append(encode)
            else:
                classnames.pop(index)
        else:
            classnames.pop(index)
    return encodeList

encodeListKnow = Mahoa(images)
print("ma hoa thanh cong")
print(len(encodeListKnow))

# save encodeListKnow + classnames in file know_face_encode.csv
# Create a DataFrame to store the face encodings
df = pd.DataFrame(encodeListKnow)
dfname = pd.DataFrame(classnames)


# thêm encode vào cuối file know_face_encode.csv
# thêm classname vào cuồi file know_face_classnames.csv
for encode in encodeListKnow:
    save_know_face_encode(encode)
for name in classnames:
    save_know_face_classname(name)