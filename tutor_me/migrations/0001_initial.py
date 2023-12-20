# Generated by Django 4.1.6 on 2023-03-30 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='default@example.com', max_length=255)),
                ('has_type', models.BooleanField(default=False)),
                ('tutor', models.BooleanField(default=False)),
                ('student', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.TextField()),
                ('experience', models.TextField()),
                ('hourly_rate', models.TextField()),
                ('location', models.TextField()),
                ('start_time', models.TextField()),
                ('end_time', models.TextField()),
                ('day', models.TextField()),
                ('availability', models.TextField(default='Available')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor_me.customuser')),
            ],
        ),
    ]
