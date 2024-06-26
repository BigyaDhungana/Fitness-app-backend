# Generated by Django 5.0.3 on 2024-03-26 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
                ('focus', models.CharField(choices=[('abs', 'abs'), ('shoulder_and_back', 'shoulder and back'), ('chest', 'chest'), ('legs', 'legs'), ('arms', 'arms')], max_length=20)),
                ('gif', models.ImageField(upload_to='gifs')),
            ],
        ),
    ]
