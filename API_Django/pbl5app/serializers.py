from .models import User, Encode, Attendance, AttendanceImage
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'role', 'password', 'fullname', 'url_video', 'phone', 'create_at', 'update_at']

class UserPasswordUpdateSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password')

class EncodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encode
        fields = ['id', 'id_user', 'encode_user']

class AttendanceSerializer(serializers.ModelSerializer):
    date = serializers.DateField(source='date_time', format='%Y-%m-%d')

    class Meta:
        model = Attendance
        fields = ('id', 'id_user', 'date')


class AttendanceImageSerializer(serializers.ModelSerializer):
    checkin = serializers.DateTimeField(source='checkin_time', format='%Y-%m-%d %H:%M')

    class Meta:
        model = AttendanceImage
        fields = ('id', 'id_user', 'image', 'checkin')

class UnconfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encode
        fields = ['id', 'id_user']