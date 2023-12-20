from datetime import datetime
from django.forms import ModelForm, ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser, Session


# class postloginForm(forms.Form):
#     CHOICES = [
#         ('1', 'Tutor'),
#         ('2', 'Student'),
#     ]
#     like = forms.ChoiceField(
#         widget=forms.RadioSelect,
#         choices=CHOICES,
#     )


class NewUserForm(forms.ModelForm):
    CHOICES = [
        ('1', 'as a Tutor'),
        ('2', 'as a Student'),
    ]
    Role = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'style':'margin-top: 30px; ' }),
        choices=CHOICES 
    )
    name = forms.CharField(required=True, max_length=20, widget=forms.TextInput(attrs={
            'placeholder':'What should we call you?', 'size':27
    })
    )
    year_CHOICES = [#I am a...
        ('1st year','1st year student'), 
        ('2nd year','2nd year student'), 
        ('3rd year','3rd year student'), 
        ('4th year', '4th year student'), 
        ('5th year', '5th year student'), 
        ('6th year', '6th year student'), 
        ('Masters degree student','Masters student'),
        ('PhD candidate','PhD candidate'),
        ("", '-----'),
        ("", 'Other',)
        
    ]
    year = forms.CharField(label='I am a', widget=forms.Select(choices=year_CHOICES), required=False)
    major = forms.CharField(required=False, max_length=50, widget=forms.TextInput(attrs={
            'placeholder':'What is/are your major(s)', 'size':27
    })
    )
    about_me = forms.CharField(widget=forms.Textarea(attrs={
            'placeholder':'Tell us a bit about yourself so others can get to know you. For example: \nWhat are your hobbies, interests, and favorites? \nWhere are you from? \nWhat subjects do you like? \nShare however much or little you would like, up to 1000 characters.'
    }), label = 'About Me', max_length=1000, required=False,
    )
    phone_num = forms.CharField(label='Phone Number', required=False, max_length=50, widget=forms.TextInput(attrs={
            'placeholder':'(123) 456-7890', 'size':20
    })
    )
    
    sm_platform_CHOICES = [
        ('Discord: ', 'Discord'),
        ('Facebook: ', 'Facebook'),
        ('Facebook Messenger: ', 'Facebook Messenger'),
        ('Instagram: ','Instagram'), 
        ('LinkedIn: ', 'LinkedIn'),
        ('Mastodon: ', 'Mastodon'),
        ('Pinterest: ', 'Pinterest'),
        ('QQ: ', 'QQ'),
        ('Reddit: ', 'Reddit'),
        ('Snapchat: ', 'Snapchat'),
        ('Telegram: ', 'Telegram'),
        ('TikTok: ', 'TikTok'),
        ('Tumblr: ', 'Tumblr'),
        ('Twitch: ', 'Twitch'),
        ('Twitter: ', 'Twitter'),
        ('WeChat: ', 'WeChat'),
        ('Weibo: ', 'Weibo'),
        ('WhatsApp: ', 'WhatsApp'),
        ('Youtube: ', 'Youtube'),
        ("", '-----')
        
    ]
    sm_platform = forms.CharField(label='Platform of main social media account', widget=forms.Select(choices=sm_platform_CHOICES), required=False)
    social_media = forms.CharField(label='Social media account username', required=False, widget=forms.TextInput(attrs={
            'placeholder':'@username', 'size':20          

    })
    )
    picture = forms.ImageField(required=False, label="Profile Photo")
    agree = forms.BooleanField(required=True, label='I understand and agree to the Tutor Me terms.')
    # email = forms.EmailField()
    # has_type = forms.BooleanField()
    # tutor = forms.BooleanField()
    # student = forms.BooleanField()

    class Meta:
        model = CustomUser
        fields = ["email", "has_type", "tutor", "student", "name", "about_me", "social_media", "picture", "phone_num", "year", "sm_platform", "major"]

        # fields = ("Tutor",'username',)
        # fields = ('email', 'has_type', 'tutor', 'student')
        exclude = ['email', 'has_type', 'day']

        def save(self, commit=True):
            user = super(NewUserForm, self).save(commit=False)
            if commit:
                user.save()
            return user


class TutorAppendForm(forms.ModelForm):

    class Meta:
        model = Session
        fields = '__all__'
        exclude = ['tutor', 'course', 'availability', 'student']

    CHOICES = (
        (' Tutor has been a TA for this course', ' I have been a TA for this course'),
        (' Tutor recieved an A+/A in the course', 'I received an A+/A in the course'),
        (' Tutor recieved an A-/B+ in the course', 'I received an A-/B+ in the course'),
        (' Tutor recieved a B/B- in the course', 'I received a B/B- in the course'),
        (' Tutor recieved a C+/C in the course', 'I received a C+/C in the course'),
        (' Tutor recieved a C- or lower in the course', 'I received a C- or lower in the course'),
        ('Tutor has not taken this class but reports knowledge of the course material', 'I have not taken this course but am knowledgable about the course material'),
    )

    experience = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'style': 'color: white;'}), required=True)
    hourly_rate = forms.CharField(required=True, max_length=20, label="Hourly rate $",
    widget=forms.TextInput(attrs={
        'class':'filter filter_hourly_rate',
        'placeholder':'Must be a number',
        'pattern':'^\$?\d{1,3}(?:,?\d{3})*(?:\.\d{2})?$' # does not accept numbers that arent real dollar amounts 
                #only positive numbers, allows commas, no more than 2 decimal digits (cents) 
    })
    )

    TIME_CHOICES = [
        ('12:00 AM', '12:00 AM'),
        ('12:15 AM', '12:15 AM'),
        ('12:30 AM', '12:30 AM'),
        ('12:45 AM', '12:45 AM'),
        ('1:00 AM', '1:00 AM'),
        ('1:15 AM', '1:15 AM'),
        ('1:30 AM', '1:30 AM'),
        ('1:45 AM', '1:45 AM'),
        ('2:00 AM', '2:00 AM'),
        ('2:15 AM', '2:15 AM'),
        ('2:30 AM', '2:30 AM'),
        ('2:45 AM', '2:45 AM'),
        ('3:00 AM', '3:00 AM'),
        ('3:15 AM', '3:15 AM'),
        ('3:30 AM', '3:30 AM'),
        ('3:45 AM', '3:45 AM'),
        ('4:00 AM', '4:00 AM'),
        ('4:15 AM', '4:15 AM'),
        ('4:30 AM', '4:30 AM'),
        ('4:45 AM', '4:45 AM'),
        ('5:00 AM', '5:00 AM'),
        ('5:15 AM', '5:15 AM'),
        ('5:30 AM', '5:30 AM'),
        ('5:45 AM', '5:45 AM'),
        ('6:00 AM', '6:00 AM'),
        ('6:15 AM', '6:15 AM'),
        ('6:30 AM', '6:30 AM'),
        ('6:45 AM', '6:45 AM'),
        ('7:00 AM', '7:00 AM'),
        ('7:15 AM', '7:15 AM'),
        ('7:30 AM', '7:30 AM'),
        ('7:45 AM', '7:45 AM'),
        ('8:00 AM', '8:00 AM'),
        ('8:15 AM', '8:15 AM'),
        ('8:30 AM', '8:30 AM'),
        ('8:45 AM', '8:45 AM'),
        ('9:00 AM', '9:00 AM'),
        ('9:15 AM', '9:15 AM'),
        ('9:30 AM', '9:30 AM'),
        ('9:45 AM', '9:45 AM'),
        ('10:00 AM', '10:00 AM'),
        ('10:15 AM', '10:15 AM'),
        ('10:30 AM', '10:30 AM'),
        ('10:45 AM', '10:45 AM'),
        ('11:00 AM', '11:00 AM'),
        ('11:15 AM', '11:15 AM'),
        ('11:30 AM', '11:30 AM'),
        ('11:45 AM', '11:45 AM'),
        ('12:00 PM', '12:00 PM'),
        ('12:15 PM', '12:15 PM'),
        ('12:30 PM', '12:30 PM'),
        ('12:45 PM', '12:45 PM'),
        ('1:00 PM', '1:00 PM'),
        ('1:15 PM', '1:15 PM'),
        ('1:30 PM', '1:30 PM'),
        ('1:45 PM', '1:45 PM'),
        ('2:00 PM', '2:00 PM'),
        ('2:15 PM', '2:15 PM'),
        ('2:30 PM', '2:30 PM'),
        ('2:45 PM', '2:45 PM'),
        ('3:00 PM', '3:00 PM'),
        ('3:15 PM', '3:15 PM'),
        ('3:30 PM', '3:30 PM'),
        ('3:45 PM', '3:45 PM'),
        ('4:00 PM', '4:00 PM'),
        ('4:15 PM', '4:15 PM'),
        ('4:30 PM', '4:30 PM'),
        ('4:45 PM', '4:45 PM'),
        ('5:00 PM', '5:00 PM'),
        ('5:15 PM', '5:15 PM'),
        ('5:30 PM', '5:30 PM'),
        ('5:45 PM', '5:45 PM'),
        ('6:00 PM', '6:00 PM'),
        ('6:15 PM', '6:15 PM'),
        ('6:30 PM', '6:30 PM'),
        ('6:45 PM', '6:45 PM'),
        ('7:00 PM', '7:00 PM'),
        ('7:15 PM', '7:15 PM'),
        ('7:30 PM', '7:30 PM'),
        ('7:45 PM', '7:45 PM'),
        ('8:00 PM', '8:00 PM'),
        ('8:15 PM', '8:15 PM'),
        ('8:30 PM', '8:30 PM'),
        ('8:45 PM', '8:45 PM'),
        ('9:00 PM', '9:00 PM'),
        ('9:15 PM', '9:15 PM'),
        ('9:30 PM', '9:30 PM'),
        ('9:45 PM', '9:45 PM'),
        ('10:00 PM', '10:00 PM'),
        ('10:15 PM', '10:15 PM'),
        ('10:30 PM', '10:30 PM'),
        ('10:45 PM', '10:45 PM'),
        ('11:00 PM', '11:00 PM'),
        ('11:15 PM', '11:15 PM'),
        ('11:30 PM', '11:30 PM'),
        ('11:45 PM', '11:45 PM'),
    ]

    location = forms.CharField(required=True, max_length=100,
         widget=forms.TextInput(attrs={
            'placeholder':'Name or address'
    })
    )
    start_time = forms.TimeField(required=True)
    end_time = forms.TimeField(required=True)

    day_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    ]

    day = forms.CharField(label='Day of Week', widget=forms.Select(choices=day_CHOICES), required=True)
    start_time = forms.CharField(label='Start Time', widget=forms.Select(choices=TIME_CHOICES), required=True)
    end_time = forms.CharField(label='End Time', widget=forms.Select(choices=TIME_CHOICES), required=True)

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_time")
        end = cleaned_data.get("end_time")

        start_in_time = datetime.strptime(start, "%I:%M %p")
        end_in_time = datetime.strptime(end, "%I:%M %p")

        start_out_time = datetime.strftime(start_in_time, "%H:%M")
        end_out_time = datetime.strftime(end_in_time, "%H:%M")

        start_hour = int(str(start_out_time).split(':')[0])
        end_hour = int(str(end_out_time).split(':')[0])

        start_minutes = int(str(start_out_time).split(':')[1])
        end_minutes = int(str(end_out_time).split(':')[1])

        if start_hour > end_hour:
            raise ValidationError('Scheduled Time Error: Please be sure chosen "End Time" is after chosen "Start Time."')
        if start_hour == end_hour and start_minutes >= end_minutes:
            raise ValidationError('Scheduled Time Error: Please be sure chosen "End Time" is after chosen "Start Time."')


    def save(self, commit=True):
        instance = super(TutorAppendForm,self).save(commit=False)
        #new_class = self.cleaned_data['course']
        #new_class_experience = self.cleaned_data['new_class_experience']

        #print("new class", new_class)
        #print("experience level",new_class_experience)

        #instance.classesTaught[new_class] = new_class_experience

        if commit:
            instance.save()
        return instance