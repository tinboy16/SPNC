# Generated by Django 3.1.3 on 2023-11-24 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0028_auto_20231124_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='standard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subject', to='curriculum.standard'),
        ),
    ]
