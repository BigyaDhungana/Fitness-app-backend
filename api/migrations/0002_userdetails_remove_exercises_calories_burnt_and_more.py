# Generated by Django 5.0.3 on 2024-03-26 06:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('height', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='exercises',
            name='calories_burnt',
        ),
        migrations.RemoveField(
            model_name='exercises',
            name='reps',
        ),
        migrations.AlterField(
            model_name='exercises',
            name='focus',
            field=models.CharField(choices=[('abs', 'abs'), ('arms_and_back', 'arms and back'), ('chest', 'chest'), ('legs', 'legs')], max_length=15),
        ),
        migrations.CreateModel(
            name='UserDaily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('steps', models.IntegerField(default=0)),
                ('calories', models.DecimalField(decimal_places=3, default=0, max_digits=5)),
                ('water', models.IntegerField(default=0)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
