# Generated by Django 4.1.6 on 2023-04-16 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_me', '0006_customuser_about_me_customuser_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(null=True, upload_to='media/Tutor Me/static/tutor_me/images/uploads/'),
        ),
    ]
