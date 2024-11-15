# Generated by Django 3.1.3 on 2023-11-24 09:08

import curriculum.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0026_auto_20231017_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='position',
            field=models.PositiveSmallIntegerField(verbose_name='Số Bài'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=models.ImageField(blank=True, upload_to=curriculum.models.save_subject_image, verbose_name='Ảnh bài học'),
        ),
    ]
