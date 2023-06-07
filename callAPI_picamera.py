import requests
import time
from picamera import PiCamera

# Đường dẫn của API
url = "http://192.168.43.250:8000/receive_image/?image/"

# Khởi tạo camera
camera = PiCamera()

# Vòng lặp chụp ảnh và gửi lên server mỗi giây một lần
while True:
    # Chụp ảnh từ camera
    image_path = '/home/nhom13tt/Downloads/image.jpg'
    camera.capture(image_path)

    # Gửi ảnh lên server
    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
        r = requests.post(url, files=files)
        print(r.json())  # In kết quả nhận được từ server
    
    time.sleep(1)  # Đợi 1 giây trước khi chụp và gửi ảnh tiếp theo

# Kết thúc chương trình
camera.close()
