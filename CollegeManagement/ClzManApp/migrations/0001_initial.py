# Generated by Django 3.0.1 on 2020-01-11 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentID', models.CharField(max_length=50)),
                ('StudentName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('standard', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeacherID', models.CharField(max_length=50)),
                ('TeacherName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('department', models.CharField(max_length=255)),
            ],
        ),
    ]