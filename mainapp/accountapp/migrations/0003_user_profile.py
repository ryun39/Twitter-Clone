# Generated by Django 4.0.5 on 2022-08-08 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0002_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Profile',
            field=models.FileField(default=1, upload_to='Profile'),
            preserve_default=False,
        ),
    ]
