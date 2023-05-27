import cv2
import requests
import time

# url = "http://192.168.83.250:8000/receive_image/?image/" # run by ip 
# Đường dẫn của API
url = "http://localhost:8000/receive_image/?image/"
# url = "https://8fab-117-2-255-218.ngrok-free.app/receive_image/?image/"

# Khởi tạo camera
cap = cv2.VideoCapture(0)

# Vòng lặp chụp ảnh và gửi lên server mỗi giây một lần
while True:
    # Chụp ảnh từ camera
    ret, frame = cap.read()
    if not ret:
        break
    
    # Gửi ảnh lên server
    _, img_encoded = cv2.imencode('.jpg', frame)
    files = {'image': ('image.jpg', img_encoded.tostring(), 'image/jpeg', {'Expires': '0'})}
    r = requests.post(url, files=files)
    print(r.json())  # In kết quả nhận được từ server
    
    time.sleep(1)  # Đợi 1 giây trước khi chụp và gửi ảnh tiếp theo

# Giải phóng camera và kết thúc chương trình
cap.release()
cv2.destroyAllWindows()
