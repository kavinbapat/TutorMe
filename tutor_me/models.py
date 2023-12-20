from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import HStoreField
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, timedelta
from django.utils import timezone
#from django.core.exceptions import ValidationError


# Create your models here.
class CustomUser(models.Model):
    email = models.EmailField(max_length=255, default="default@example.com")
    has_type = models.BooleanField(default=False)
    tutor = models.BooleanField(default=False)
    student = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='Tutor Me/static/tutor_me/images/uploads/', default='Tutor Me/static/tutor_me/images/uploads/default.jpg')
    name = models.TextField(max_length=255, default="User")
    about_me = models.TextField(max_length=1000, default="UVA Student")
    year = models.TextField(max_length=100, default="")
    major = models.TextField(max_length=225, default="")
    phone_num = models.TextField(max_length=50, default="")
    sm_platform =models.TextField(max_length=50, default="")
    social_media = models.TextField(max_length=50, default="")


    def __str__(self):
        return self.email
        # return "Has Type: " + str(self.has_type) + "\nTutor: " + str(self.tutor) + "\nStudent: " + str(self.student)


class Session(models.Model):
    tutor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="admin_user")
    course = models.TextField()
    experience = models.TextField()
    hourly_rate = models.TextField()
    location = models.TextField()
    start_time = models.TextField()
    end_time = models.TextField()
    day = models.TextField()
    availability = models.TextField(default="Available")
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name="common_user")

    # def clean(self):
    #     start = self.start_time.split(':')[0]
    #     end = self.end_time.split(':')[0]

    #     start_ampm = self.start_time.split(' ')[1]
    #     end_ampm = self.end_time.split(' ')[1]

    #     if start >= end and start_ampm == end_ampm:
    #         raise ValidationError('Start time must be before end time')
    #     elif start_ampm == 'PM' and end_ampm == 'AM':
    #         raise ValidationError('Start time must be before end time')
        
    #     return super().clean()
    
    #add proposed start date?
    def __str__(self):
    #    return "Course: " + self.course + " - Tutor: " + self.tutor.email + "\n\tHourly Rate: " \
    #        + self.hourly_rate + "\n\tLocation: " + self.location + "Day: " + self.day + "\n\tTime Slot: " \
    #    + self.start_time + " - " + self.end_time + "\n\tAvailability" + self.availability
        return "Course: " + self.course + ", Tutor: " + self.tutor.email

class Notification(models.Model):
    tutor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null = True, related_name="notification_admin_user")
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name="notification_common_user")
    text = models.TextField(max_length=500, null=True)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, null = True)


class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_mnemonic = models.CharField(max_length=10)
    def __str__(self):
        return self.dept_name

class Course(models.Model):
    course_info = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, db_index=True)

    def __str__(self):
        return self.course_info