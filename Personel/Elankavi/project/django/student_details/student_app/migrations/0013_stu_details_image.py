# Generated by Django 3.2.4 on 2021-07-23 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0012_alter_stu_details_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='stu_details',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]