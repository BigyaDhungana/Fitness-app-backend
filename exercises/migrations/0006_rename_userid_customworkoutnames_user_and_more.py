# Generated by Django 5.0.3 on 2024-04-06 14:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0005_customworkoutnames_customworkouts'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='customworkoutnames',
            old_name='userid',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='customworkoutnames',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='customworkoutnames',
            unique_together={('name', 'user')},
        ),
    ]
