from django.contrib import admin
# Register your models here.
from .models import User, Encode, AttendanceImage
 
admin.site.register(User)
admin.site.register(Encode)



from .models import Attendance
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'date_time')  # Danh sách các trường muốn hiển thị
admin.site.register(Attendance, AttendanceAdmin)

class AttendanceImageAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'checkin_time')  # Danh sách các trường muốn hiển thị
admin.site.register(AttendanceImage, AttendanceImageAdmin)

from .models import Unconfirm
class UnconfirmAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_user')  # Danh sách các trường muốn hiển thị
admin.site.register(Unconfirm, UnconfirmAdmin)