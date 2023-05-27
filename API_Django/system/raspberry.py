# nhiệm vụ của raspberry là kết nối với camera lấy video
# raspberry sẽ lấy liên tục 10 tấm ảnh trong vòng 1s
# với mỗi tấm ảnh thì sẽ kiểm tra thử có khuôn mặt nào trong ảnh không
# nếu có thì sẽ lấy được tọa độ của các khuôn mặt trên đó
# trích xuất đặc trưng cho các khuôn mặt đó tạo thành danh sách các đặc trưng của các khuôn mặt
# sau đó truyền danh sách các đặc trưng của các khuôn mặt này về cho server xử lí

# cải thiện:
# thay vì gửi liên tục tất cả những đặc trưng của khuôn mặt phát hiện được thì có thể lọc ra như sau:
# + nếu khuôn mặt xuất hiện ở frame sau có tọa độ tương tự (có di chuyển nhỏ) so với frame trước đó thì loại khuôn mặt đó ra
# + yêu cầu: phải lưu lại tọa độ của các khuôn mặt của frame trước, để loại bỏ các khuôn mặt của các frame sau có cùng tọa độ


import cv2
import face_recognition
from datetime import datetime
import csv

# hàm lưu encode
# def save_encode_face(encode):
#     # Hàng mới cần thêm vào
#     new_row = encode

#     # Mở file CSV trong chế độ "append"
#     with open("../../AnacondaFace/system/SaveDir/face_rasp_recog.csv", 'a', newline='') as file:
#         writer = csv.writer(file)

#         # Ghi hàng mới vào cuối file
#         writer.writerow(new_row)


# Khởi động webcam
# cap = cv2.VideoCapture("videotest2s.mp4")
cap = cv2.VideoCapture(0)
dem = 0

while(True):
    # trả về boolean và khung hình: (false , none) hoặc (true, image)
    ret, frame = cap.read()
    print(datetime.now())
    # if dem < 3:
    #     dem += 1
    #     continue
    # else:
    #     dem = 0
    # framS = cv2.resize(frame, (0, 0), None, fx=0.5, fy=0.5)
    framS = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    facecurFrame = face_recognition.face_locations(framS)       #danh sach toa do cac khuon mat tren khung hinh hien tai
    encodecurFrame = face_recognition.face_encodings(framS)     #danh sach dac trung cac khuon mat tren khung hinh hien tai

    for encodeFace, faceLoc in zip(encodecurFrame, facecurFrame):
        # matches = face_recognition.compare_faces(encodeListKnow, encodeFace)
        # print(matches)
        # faceDis = face_distance_again(encodeListKnow, encodeFace)
        # print(faceDis)
        # matchIndex = np.argmin(faceDis)
        # if faceDis[matchIndex]<0.50 :
        #     name = classnames[matchIndex].upper()
        #     thamdu(name)
        # else:
        #     name = "UNKNOW"
        #print ten len frame
        y1, x2, y2, x1 = faceLoc
        # y1, x2, y2, x1 = y1*2, x2*2, y2*2, x1*2
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)
        # cv2.putText(frame, name, (x2, y2), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
        # save_encode_face(encodeFace)   # gui cho server
        print (encodeFace)
        cv2.imshow("Phuc lap trinh", frame)
    if cv2.waitKey(1)==ord("q"): #độ trễ 1/1000s, nếu bấm q sẽ thoát
        break
cap.release() #giai phong camera
cv2.destroyAllWindows() #thoat tat ca cua soq