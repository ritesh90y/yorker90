# Generated by Django 3.0.2 on 2020-01-25 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobapp', '0004_auto_20200117_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
