# Trong models.py
from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # lấy tên file
    if instance.pk:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.pk, ext)
    return os.path.join(upload_to, filename)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)
    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="Ảnh đại diện", blank=True)
    
    teacher = 'teacher'
    student = 'student'
    user_types = [
        (teacher, 'giảng viên'),
        (student, 'người học'),
    ]
    user_type = models.CharField(max_length=10, choices=user_types, default=student)
    
    def __str__(self):
        return self.user.username

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)  # Thay đổi từ CharField thành EmailField và thêm unique=True
    feedback = models.TextField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('index')
