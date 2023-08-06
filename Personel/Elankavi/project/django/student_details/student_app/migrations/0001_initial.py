# Generated by Django 3.2.4 on 2021-07-21 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stu_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=10)),
                ('DOB', models.DateField()),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'others')], max_length=100)),
            ],
        ),
    ]