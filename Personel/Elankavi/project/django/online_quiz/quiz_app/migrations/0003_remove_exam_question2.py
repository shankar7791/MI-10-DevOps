# Generated by Django 3.2.4 on 2021-07-01 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_exam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='question2',
        ),
    ]
