from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, LoginView, UserList, AdminList, UserUpdateAPIView, UserPasswordUpdateAPIView, receive_image
from .views import AttendanceByMonthAPIView
from .views import attendance_count
from .views import attendance_count_by_month
from .views import attendance_day, attendance_month, attendance_year, num_user, AttendanceImageViewSet, UnconfirmViewSet, AttendanceViewSet, getFullnameById

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'unconfirms', UnconfirmViewSet)
router.register(r'checkins', AttendanceImageViewSet, basename='attendanceimage')



urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('user-list/', UserList.as_view(), name='user-list'),
    path('admin-list/', AdminList.as_view(), name='admin-list'),
    path('users/<int:pk>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('users/<int:pk>/password-change/', UserPasswordUpdateAPIView.as_view(), name='user-change-password'),
    # path('receive_encode_face/', receive_encode_face, name='receive_encode_face'),
    path('receive_image/', receive_image, name='receive_imgae'),
    path('attendance/<int:user_id>/<int:year>/<int:month>/', AttendanceByMonthAPIView.as_view(), name='attendance-by-month'),
    path('week-absentee/', attendance_count, name='attendance_count'),
    path('year-absentee/', attendance_count_by_month, name='attendance_count_by_month'),
    path('attendance-day/', attendance_day, name='attendance_day'),
    path('attendance-month/', attendance_month, name='attendance_month'),
    path('attendance-year/', attendance_year, name='attendance_year'),
    path('num-user/', num_user, name='num-user'),
    path('full-name/', getFullnameById, name='full-name'),
    
]