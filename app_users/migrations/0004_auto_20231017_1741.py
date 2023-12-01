# Generated by Django 3.1.3 on 2023-10-17 17:41

import app_users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=app_users.models.path_and_rename, verbose_name='Ảnh đại diện'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_type',
            field=models.CharField(choices=[('teacher', 'giáo viên'), ('student', 'học sinh'), ('parent', 'phụ huynh')], default='student', max_length=10),
        ),
    ]