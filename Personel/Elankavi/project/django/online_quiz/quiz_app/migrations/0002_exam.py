# Generated by Django 3.2.4 on 2021-07-01 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('question1', models.CharField(max_length=100)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('corrans', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'onlineexam',
            },
        ),
    ]
