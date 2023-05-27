from django.db import models

import hashlib

def hash_password(password):
    salt = "random string to make the hash more secure"
    salted_password = password + salt
    hashed_password = hashlib.sha256(salted_password.encode('utf-8')).hexdigest()
    return hashed_password

def hash_password_if_changed(password):
    if isinstance(password, str):
        salt = "random string to make the hash more secure"
        salted_password = password + salt
        hashed_password = hashlib.sha256(salted_password.encode('utf-8')).hexdigest()
        return hashed_password
    else:
        return password


class User(models.Model):

    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=5, default="user")
    password = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255, null=True, blank=True)
    url_video = models.FileField(upload_to='static/videos/', null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = hash_password(self.password)
        else:
            existing_user = User.objects.get(pk=self.pk)
            if existing_user.password != self.password:
                self.password = hash_password_if_changed(self.password)
        super(User, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.id)
    

class Encode(models.Model):
    id = models.AutoField(primary_key=True)
    id_user =  models.IntegerField(null=True, blank=True)
    encode_user = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
    

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    id_user =  models.IntegerField(null=True, blank=True)
    date_time = models.DateTimeField()

    def __str__(self):
        return str(self.id)
    


class AttendanceImage(models.Model):
    id = models.AutoField(primary_key=True)
    id_user =  models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='static/images/', null=True)
    checkin_time = models.DateTimeField()

    def __str__(self):
        return str(self.id)
    

    
class Unconfirm(models.Model):
    id = models.AutoField(primary_key=True)
    id_user =  models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
