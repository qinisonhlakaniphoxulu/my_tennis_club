# Generated by Django 5.0.6 on 2024-07-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='phone',
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
