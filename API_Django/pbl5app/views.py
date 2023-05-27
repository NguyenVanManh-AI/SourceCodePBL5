from rest_framework import viewsets
from django.core.mail import send_mail
from .models import User, Encode, Attendance, AttendanceImage, Unconfirm
from .serializers import UserSerializer, UserPasswordUpdateSerializer, EncodeSerializer, AttendanceImageSerializer, UnconfirmSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UnconfirmViewSet(viewsets.ModelViewSet):
    queryset = Unconfirm.objects.all()
    serializer_class = UnconfirmSerializer

import hashlib

def hash_password(password):
    salt = "random string to make the hash more secure"
    salted_password = password + salt
    hashed_password = hashlib.sha256(salted_password.encode('utf-8')).hexdigest()
    return hashed_password

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from django.contrib.auth import authenticate
import face_recognition
import datetime

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_401_UNAUTHORIZED)

        if hash_password(password) == user.password:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': user.password, 'errorx': hash_password(password)}, status=status.HTTP_401_UNAUTHORIZED)


from rest_framework import generics

class EncodeList(generics.ListAPIView):
    queryset = Encode.objects.all()
    serializer_class = EncodeSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.filter(role='user').order_by('-id')
    serializer_class = UserSerializer

    
class AdminList(generics.ListAPIView):
    queryset = User.objects.filter(role='admin').order_by('-id')
    serializer_class = UserSerializer

class AttendanceImageViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceImageSerializer

    def get_queryset(self):
        today = datetime.date.today()
        queryset = AttendanceImage.objects.filter(checkin_time__date=today).order_by('checkin_time')
        
        id_user = self.request.query_params.get('id_user', None)
        if id_user is not None:
            queryset = queryset.filter(id_user=id_user)
        
        return queryset


import os
from django.conf import settings

# from .ListEncodeFromVideo import ListEncodeVideo

import cv2
import os
from keras_vggface import utils
import tensorflow as tf

from tensorflow.keras.models import load_model
# returns a compiled model identical to the previous one
model = load_model(r'pbl5app\senet50_transfer_learning_trained_face_cnn_model.h5')

resize = 300
def Mahoa(images):
    list_encodes = []
    for image in images:
        framS = cv2.resize(image, (0, 0), None, fx=0.5, fy=0.5)
        framS = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encodes = face_recognition.face_encodings(framS)
        for encode in encodes:
            list_encodes.append(encode)
    return list_encodes


def MaHoaSeNet50(images):
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


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        update_encode= 0
        if 'url_video' in request.data:
            try:
                unconfirm = Unconfirm.objects.get(id_user=str(instance.id))
                # Thực hiện các hành động với user tìm thấy
            except Unconfirm.DoesNotExist:
                # Xử lý trường hợp không tìm thấy user
                unconfirm = Unconfirm(id_user=str(instance.id))
                unconfirm.save()

            update_encode= 1
            if instance.url_video:
                # Xoa encode cu
                Encode.objects.filter(id_user=str(instance.id)).delete()
              
                # Xóa video cũ
            
                path = instance.url_video.path
                if os.path.isfile(os.path.join(settings.MEDIA_ROOT, path)):
                    os.remove(os.path.join(settings.MEDIA_ROOT, path))
                

            # Lưu video mới
            instance.url_video = request.data['url_video']
            

        serializer.save()   # NOTE: update_encode de sau dong nay thi path moi chinh xac

        if update_encode==1:
            
            # tao encode moi        
            path = instance.url_video.path
            cap = cv2.VideoCapture(path)
            list_encodes = ListEncodeVideo(cap)
            for vector in list_encodes:
                new_encode = Encode(encode_user=str(vector), id_user=instance.id)
                new_encode.save()   
                
        return Response(serializer.data)






class UserPasswordUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserPasswordUpdateSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        old_password = hash_password(request.data.get('old_password'))
        new_password = request.data.get('new_password')
        if old_password == instance.password:
            instance.password = new_password
            instance.save(update_fields=['password'])
            # serializer = self.get_serializer(instance)
            return Response({'message': 'Password Changed'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Incorrect Old Password'}, status=status.HTTP_400_BAD_REQUEST)
        
# import csv
# def save_encode_face(encode):
#     # Hàng mới cần thêm vào
#     new_row = encode

#     # Mở file CSV trong chế độ "append"
#     with open("./face_rasp_recog.csv", 'a', newline='') as file:
#         writer = csv.writer(file)

#         # Ghi hàng mới vào cuối file
#         writer.writerow(new_row)

# import base64
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import numpy as np

# @csrf_exempt
# def receive_encode_face(request):
#     if request.method == 'POST':
#         # Lấy dữ liệu encodeFace_bytes từ request POST
        
#         encodeFace_str = request.POST.get('encodeFace', None)
    

#         # Kiểm tra xem dữ liệu encodeFace_bytes có tồn tại hay không
#         if encodeFace_str is None:
#             return JsonResponse({'error': 'encodeFace_str == None'})
#         # Giải mã đối tượng bytes thành mảng numpy
#         encodeFace = np.fromstring(encodeFace_str[1:-1], sep=' ')
        
#         save_encode_face(encodeFace)
#             # Do something with encode_face , 'encode_face':encode_face
#         return JsonResponse({'status': 'success'})
#     else:
#         return JsonResponse({'status': 'error'})

import io

# def EncodeFrame(framS):
#     return face_recognition.face_encodings(framS)

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
        list_encode.append(encode)
    return list_encode

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import numpy as np

import re
@csrf_exempt
def receive_image(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            image_file = request.FILES['image']
            # Chuyển đổi image_file thành framS
            image_bytes = io.BytesIO(image_file.read())
            framS = face_recognition.load_image_file(image_bytes)
            # cv2.imwrite("DEMOtruoc.jpg", framS)
            
            framS = cv2.resize(framS, (0, 0), None, fx=0.5, fy=0.5)
            framS = cv2.cvtColor(framS, cv2.COLOR_BGR2RGB)
            # cv2.imwrite("DEMO.jpg", framS)
            # Tính toán face encodings
            list_encode = EncodeFrameSenet50(framS)
            # lấy danh sách encode
            # nhận diện list_encode thành id tương ứng
            # thêm id vào danh sách điểm danh
            listEncodeRasp = []
            for val in list_encode: 
                listEncodeRasp.append(list(val))
            
            
            encodes = Encode.objects.all()
            listAttendanceImage = AttendanceImage.objects.all()
            list_userId = []
            list_userEncode = []
            for encode in encodes:
                data = encode.encode_user

                # Xóa ký tự "[" và "]" khỏi chuỗi dữ liệu
                data = data.replace("[", "").replace("]", "")

                # Chuyển chuỗi dữ liệu thành một danh sách các giá trị float
                data = [float(x) for x in data.split()]

                # Chuyển danh sách thành một numpy array
                np_array = np.array(data, dtype=np.float32)
                list_userEncode.append(np_array)  
                                
                list_userId.append(encode.id_user)
            
            list_userEncode = np.array(list_userEncode)

            if len(listEncodeRasp)  > 0:
                for encode_raps in listEncodeRasp:
                    user_encode_array = np.array(list_userEncode)
                    raps_encode_array = np.array(list(map(float, encode_raps)))
                    faceDis = face_recognition.face_distance(user_encode_array, raps_encode_array)
                    
                    matchIndex = np.argmin(faceDis)
                    if faceDis[matchIndex] < 15:
                        found = True
                        try:
                            unconfirm = Unconfirm.objects.get(id_user=list_userId[matchIndex])
                            # Thực hiện các hành động với user tìm thấy
                        except Unconfirm.DoesNotExist:
                            # Xử lý trường hợp không tìm thấy user
                            found = False
                            pass

                        if (found):
                            continue
                            

                        new_attendance = Attendance(id_user=list_userId[matchIndex],  date_time= datetime.datetime.now())
                        new_attendance.save()

                        exists = listAttendanceImage.filter(id_user=list_userId[matchIndex],  checkin_time__date=datetime.datetime.now().date().isoformat()).exists()
                        if not exists:
                            # AttendanceImage với id_user là 5 ko tồn tại trong listAttendanceImage
                            newAttendanceImage = AttendanceImage(id_user=list_userId[matchIndex],  image= image_file, checkin_time= datetime.datetime.now())
                            newAttendanceImage.save()

                            #Send mail
                            subject = 'Successful attendance'
                            message = 'Attendance today at '+datetime.datetime.now().ctime()
                            from_email = 'pbl5.system.ai@gmail.com'

                            try:
                                user = User.objects.get(id=list_userId[matchIndex])
                                email = user.email
                                # Sử dụng biến 'email' cho mục đích mong muốn
                                recipient_list = [email]
                                send_mail(subject, message, from_email, recipient_list)
                            except User.DoesNotExist:
                                # Xử lý trường hợp không tìm thấy người dùng
                                pass
                           

            return JsonResponse({'message': 'Success', 'len':str(len(list_encode))})
        else:
            return JsonResponse({'message': 'No image found in request'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)


from rest_framework import generics
# from .models import Attendance
from .serializers import AttendanceSerializer

class AttendanceByMonthAPIView(generics.ListAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']  # Lấy id người dùng từ URL
        month = self.kwargs['month']  # Lấy tháng từ URL
        year = self.kwargs['year']  # Lấy năm từ URL

        # Lấy điểm danh theo người dùng, tháng và năm
        queryset = Attendance.objects.filter(
            id_user=user_id,
            date_time__month=month,
            date_time__year=year
        ).order_by('date_time')

        # Chỉ lấy điểm danh sớm nhất của mỗi ngày
        attendance_dates = set()
        filtered_queryset = []
        for attendance in queryset:
            date = attendance.date_time.date()
            if date not in attendance_dates:
                attendance_dates.add(date)
                attendance.date_time = date
                filtered_queryset.append(attendance)

        return filtered_queryset




from django.http import JsonResponse
from django.db.models import Count
from datetime import timedelta
from .models import Attendance

begin_day = datetime.date(2023, 1, 1) # bắt đầu tính từ ngày 1/1/2023 

def attendance_count(request):
    maxUser = User.objects.filter(role='user').count()
    # Tìm ngày đầu tiên của tuần (thứ 2)
    today = datetime.datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())

    # Tạo một danh sách để lưu số người điểm danh từ thứ 2 đến chủ nhật
    attendance_count = []

    # Lặp qua từng ngày trong tuần từ thứ 2 đến chủ nhật
    for i in range(7):
        # Tính toán ngày của từng ngày trong tuần
        today = start_of_week + timedelta(days=i)
        # Lấy số người điểm danh cho ngày hiện tại
        if (begin_day <= today) and (today <= datetime.datetime.now().date()):
            count = Attendance.objects.filter(date_time__date = today).values('id_user').annotate(count=Count('id_user')).count()
        else:
            count = maxUser
        # Thêm số người điểm danh vào danh sách
        attendance_count.append(count)

    
    for i in range(7):
        attendance_count[i]= maxUser - attendance_count[i]
    # Trả về kết quả dưới dạng JSON
    return JsonResponse(attendance_count, safe=False)



from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Attendance

import calendar

@csrf_exempt
def attendance_count_by_month(request):
    
    year = datetime.datetime.now().year
    maxUser = User.objects.filter(role='user').count()
    attendance_count = []

    for month in range(1, 13):
        # Lấy số ngày trong tháng
        num_days = calendar.monthrange(year, month)[1]

        # Lặp qua từng ngày trong tháng
        sum = 0
        for day in range(1, num_days + 1):
            today = datetime.date(year, month, day)
            
            if (begin_day <= today) and (today <= datetime.datetime.now().date()):
                count = Attendance.objects.filter(date_time__date = today).values('id_user').annotate(count=Count('id_user')).count()
            else:
                count = maxUser
            sum += count
        attendance_count.append(maxUser*num_days - sum)

    # Trả về dữ liệu dưới dạng JSON
    return JsonResponse(attendance_count, safe=False)


from datetime import date, time
def attendance_year(request):
    maxUser = User.objects.filter(role='user').count()
    year = datetime.datetime.now().year
    
    dung_gio = 0
    vang_mat = 0
    tre_gio = 0

    for month in range(1, 13):
        num_days = calendar.monthrange(year, month)[1]
        for day in range(1, num_days+1):
            
            today = datetime.date(year, month, day)
            start_time = datetime.datetime.combine(today, time(hour=8)) 


            if (begin_day <= today) and (today <= datetime.datetime.now().date()):   
           
                on_time_count = Attendance.objects.filter(date_time__date = today, date_time__lt=start_time).values('id_user').annotate(count=Count('id_user')).count()
                late_count = Attendance.objects.filter(date_time__date=today, date_time__gte=start_time).values('id_user').annotate(count=Count('id_user')).count()
    
                absent_count = maxUser - (on_time_count + late_count)
            else:
                on_time_count = 0
                late_count = 0
                absent_count = 0

            dung_gio += on_time_count
            vang_mat += absent_count
            tre_gio += late_count

    
    data = {
        'dung_gio': dung_gio,
        'vang_mat': vang_mat,
        'tre_gio': tre_gio,
    }
    return JsonResponse(data)

def attendance_month(request):
    maxUser = User.objects.filter(role='user').count()
        
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    num_days = calendar.monthrange(year, month)[1]

    dung_gio = 0
    vang_mat = 0
    tre_gio = 0
    for day in range(1, num_days+1):
        today = datetime.date(year, month, day)
        start_time = datetime.datetime.combine(today, time(hour=8)) 

        if (begin_day <= today) and (today <= datetime.datetime.now().date()):   
            on_time_count = Attendance.objects.filter(date_time__date = today, date_time__lt=start_time).values('id_user').annotate(count=Count('id_user')).count()
            late_count = Attendance.objects.filter(date_time__date=today, date_time__gte=start_time).values('id_user').annotate(count=Count('id_user')).count()
    
            absent_count = maxUser - (on_time_count + late_count)
        else:
            on_time_count = 0
            late_count = 0
            absent_count = 0

        dung_gio += on_time_count
        vang_mat += absent_count
        tre_gio += late_count

    
    data = {
        'dung_gio': dung_gio,
        'vang_mat': vang_mat,
        'tre_gio': tre_gio,
    }
    return JsonResponse(data)

def attendance_day(request):
    today = date.today()
    start_time = datetime.datetime.combine(today, time(hour=8)) 
    
    on_time_count = Attendance.objects.filter(date_time__date = today, date_time__lt=start_time).values('id_user').annotate(count=Count('id_user')).count()
    late_count = Attendance.objects.filter(date_time__date=today, date_time__gte=start_time).values('id_user').annotate(count=Count('id_user')).count()
    
    maxUser = User.objects.filter(role='user').count()
    absent_count = maxUser - (on_time_count + late_count)
    
    data = {
        'dung_gio': on_time_count,
        'vang_mat': absent_count,
        'tre_gio': late_count,
    }
    return JsonResponse(data)

def num_user(request):
    maxUser = User.objects.filter(role='user').count()
    return JsonResponse({'so_nhan_vien': str(maxUser)})

    

    