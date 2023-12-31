# Generated by Django 4.1.6 on 2023-04-11 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_me', '0005_session_student_alter_session_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about_me',
            field=models.TextField(default='UVA Student', max_length=1000),
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.TextField(default='User', max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(null=True, upload_to='Tutor Me/static/tutor_me/images/uploads/'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='social_media',
            field=models.TextField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='common_user', to='tutor_me.customuser'),
        ),
        migrations.AlterField(
            model_name='session',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_user', to='tutor_me.customuser'),
        ),
    ]
