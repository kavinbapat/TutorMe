from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
import datetime
import requests
from .forms import NewUserForm, TutorAppendForm  # ,postloginForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from .models import CustomUser, Session, Notification, Department, Course
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView

# Create your views here.
def index_view(request):
    return render(request, 'tutor_me/index.html')


class MyLogoutView(LogoutView):
    template_name = 'tutor_me/logout.html'

mylogout_view = MyLogoutView.as_view()

def searchResults(request):
    return HttpResponse('Hi, this is where your search results will be.')

def register_request(request):
    email = SocialAccount.objects.filter(user=request.user)[0].extra_data['email']
    if request.method == "POST":
        new_user = CustomUser(email=email, has_type=True)
        form = NewUserForm(request.POST, request.FILES, instance=new_user)#, instance=request.user)


        if form.is_valid():
            if form.cleaned_data.get('Role') == '1':
               new_user.tutor = True
            elif form.cleaned_data.get('Role') == '2':
                new_user.student = True
            valid_form = form.save()
        messages.success(request, "Registration successful.")
        if form.cleaned_data.get('Role') == '1':
            return  HttpResponseRedirect(reverse('tutor_me:direct'))
            #changed from render to better handle POST
            #             #render(request=request, template_name="tutor_me/tutor.html")
        else:
            return  HttpResponseRedirect(reverse('tutor_me:direct'))
            #changed from render to better handle POST
            # render(request=request, template_name="tutor_me/student.html")
    else:
        messages.error(request, "Unsuccessful registration. Invalid information.")
        form = NewUserForm()
    return render(request=request, template_name="tutor_me/register.html", context={"register_form": form})


def username_exists(username):
    return CustomUser.objects.filter(username=username).exists()


def direct_user(request):
    user_email = SocialAccount.objects.filter(user=request.user)[0].extra_data['email']
    if CustomUser.objects.filter(email=user_email).exists():
        user = CustomUser.objects.filter(email=user_email).get()
        # print(CustomUser.objects.all().values())
        if not user.has_type:
            register_request(request)
        else:
            if user.tutor:
                sessions = Session.objects.filter(tutor=user)
                notifications = Notification.objects.filter(tutor=user, read=False)

                return render(request, "tutor_me/tutor.html", {'sessions': sessions, 'user': user, 'notifications': notifications})
            else:
                sessions = Session.objects.filter(student=user)
                notifications = Notification.objects.filter(student=user, read=False)
                return render(request, "tutor_me/student.html", {'sessions': sessions, 'user': user, 'notifications':notifications})
    else:
        return register_request(request)

# Display all departments on html page
def getAllDepartments(request):
    info_list = Department.objects.all()
    departments = Department.objects.all()
    subject_list = []
    mnemonic_list = []
    # iterate through all subjects
    for d in departments:
        # append the subject mnemonic to list
        subject_list.append(d.dept_name)
        mnemonic_list.append(d.dept_mnemonic)
    info_list = zip(subject_list, mnemonic_list)
    return render(request, 'tutor_me/departments.html', {'info_list': info_list})  
 
def DepartmentSearch(request):
    # query the api and return a json file
    all_depts = Department.objects.all()
    result_depts = []
    mnemonics=[]
    query = str(request.GET.get("search"))
    for m in all_depts:
        if query.lower() in m.dept_name.lower():
            result_depts.append(m.dept_name) 
            mnemonics.append(m.dept_name.split("-",1)[0][:-1])     
    print(result_depts)
    print(mnemonics)
    results_list = zip(result_depts, mnemonics)
    print(results_list)
    # send list of subject mnemonics to html page for rendering
    return render(request, 'tutor_me/search.html', {'results_list': results_list, 'result_depts': result_depts, "query": query})



def getAllCoursesFromDepartment(request, course_subject):# Courses
    #print(type(course_subject))# string AAS - African American...
    #print(course_subject)
    department= Department.objects.filter(dept_mnemonic=course_subject)
    print(department)
    course_list = []
    course_list = Course.objects.filter(department=department[0])
    print(course_list)
    subject_name= department[0].dept_name
    subject_name= subject_name.split("-",1)[1]

    # send course_list to html template to render on screen
    return render(request, 'tutor_me/courses.html', {'course_list': course_list, 'course_subject' : course_subject, 'subject_name' : subject_name })


def CourseSearch(request, course_subject):
    results_course = [] 
    department= Department.objects.filter(dept_mnemonic=course_subject)
    print(department)
    course_list = []
    course_list = Course.objects.filter(department=department[0])
    print(course_list)
    subject_name= department[0].dept_name
    subject_name= subject_name.split("-",1)[1]

    query = str(request.GET.get("search"))
    for m in course_list:
        if query.lower() in m.course_info.lower():
            results_course.append(m.course_info)
    print(results_course)

    return render(request, 'tutor_me/search_course.html', {'results_course': results_course, 'course_subject' : course_subject, 'subject_name' : subject_name, "query": query})


def CourseInteract(request, course):
    # print(course)
    user_email = SocialAccount.objects.filter(user=request.user)[0].extra_data['email']
    Curruser = CustomUser.objects.filter(email=user_email).get()

    if Curruser.tutor:

        if request.method == 'POST':
            form = TutorAppendForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.tutor = Curruser
                form.course = course
                form.save()

                # new_class_experience = form.cleaned_data.get('I')
                # Curruser.classesTaught[course] = new_class_experience
                # Curruser.save()
                # form.save()
                return redirect('/direct/')
        else:
            form = TutorAppendForm()

        return render(request, 'tutor_me/tutorSelectCourse.html', {'form': form, 'course': course})

    else:  # current user is a student
        sessions = Session.objects.filter(course=course)
        return render(request, 'tutor_me/student_select_course.html', {'sessions': sessions, 'course': course})
        # return render(request, 'tutor_me/studentViewTutors', {'course': course, 'tutors':tutors})

def accept_session(request, id):
    user_email = SocialAccount.objects.filter(user=request.user)[0].extra_data['email']
    user = CustomUser.objects.filter(email=user_email).get()
    sessions = Session.objects.filter(tutor=user)
    session = Session.objects.get(id=id)
    session.availability = "Accepted"
    session.save()

    n_text = "Your tutor " + user.name + " has accepted your request to enroll in their " + session.start_time + " session for "  + session.course
    notification = Notification(tutor=None,student=session.student,text= n_text)
    notification.created_at = notification.created_at - datetime.timedelta(hours=4)
    notification.save()

    return redirect('/direct/')
    #return render(request, "tutor_me/tutor.html", {'sessions': sessions})

def decline_session(request, id):
    user_email = SocialAccount.objects.filter(user=request.user)[0].extra_data['email']
    user = CustomUser.objects.filter(email=user_email).get()
    sessions = Session.objects.filter(tutor=user)
    session = Session.objects.get(id=id)

    #send notification to the student that class is denied
    n_text = user.name + " has denied your request to enroll in their " + session.start_time + " session for "  + session.course
    notification = Notification(tutor=None,student=session.student,text= n_text)
    notification.created_at = notification.created_at - datetime.timedelta(hours=4)
    notification.save()

    #declare the session is available and remove the student
    session.availability = "Available"
    session.student = None
    session.save()

    return redirect('/direct/')
    #return render(request, "tutor_me/tutor.html", {'sessions': sessions})


def request_session(request, id):
    user_email = SocialAccount.objects.filter(user=request.user)[0].extra_data['email']
    user = CustomUser.objects.filter(email=user_email).get()
    session = Session.objects.get(id=id)
    print("ok")
    session.availability = "Pending"
    print("oka")
    session.student = user
    session.save()
    print("okay")
    sessions = Session.objects.filter(student=user)
    
    notification_text = user.name + " has requested to enroll in your session for " + session.course
    notification = Notification(tutor = session.tutor,student =None, text = notification_text)
    notification.created_at = notification.created_at - datetime.timedelta(hours=4)
    notification.save()
    return redirect('/direct/')


def student_cancel_session(request, id):
    user_email = SocialAccount.objects.filter(user=request.user)[0].extra_data['email']
    user = CustomUser.objects.filter(email=user_email).get()
    session = Session.objects.get(id=id)
    session.availability = "Available"
    session.student = None
    session.save()
    sessions = Session.objects.filter(student=user)

    notification_text = "Your student " + user.name + " has canceled their session with you for " + session.course
    notification = Notification(tutor = session.tutor,student =None, text = notification_text)
    notification.created_at = notification.created_at - datetime.timedelta(hours=4)
    notification.save()

    return redirect('/direct/')


def tutor_cancel_session(request, id):
    user_email = SocialAccount.objects.filter(user=request.user)[0].extra_data['email']
    user = CustomUser.objects.filter(email=user_email).get()
    session =  Session.objects.get(id=id)

    #create notification for student for the cancellation of the session
    notification_text = "Your tutor " + user.name + " has canceled their session with you for " + session.course
    notification = Notification(tutor = None,student = session.student, text = notification_text)
    notification.created_at = notification.created_at - datetime.timedelta(hours=4)
    notification.save()

    #delete the session
    deleted_session = Session.objects.get(id=id).delete()    

    return redirect('/direct/')

def student_cancel_notification(request, id):
    user_email = SocialAccount.objects.filter(user=request.user)[0].extra_data['email']
    user = CustomUser.objects.filter(email=user_email).get()
    canceled_notification = Notification.objects.get(id=id)

    canceled_notification.read = True
    canceled_notification.save()

    return redirect('/direct/')

def tutor_cancel_notification(request, id):
    user_email = SocialAccount.objects.filter(user=request.user)[0].extra_data['email']
    user = CustomUser.objects.filter(email=user_email).get()
    canceled_notification = Notification.objects.get(id=id)

    canceled_notification.read = True
    canceled_notification.save()

    return redirect('/direct/')


def view_tutor_profile_page(request, id):
    session = Session.objects.get(id=id)
    tutor = CustomUser.objects.filter(email=session.tutor).get()
    tutor_sessions = Session.objects.filter(tutor=tutor)
    return render(request, "tutor_me/view_tutor_profile.html", {'tutor': tutor, 'tutor_sessions': tutor_sessions})


def view_student_profile_page(request, id):
    session = Session.objects.get(id=id)
    student = CustomUser.objects.filter(email=session.student).get()
    return render(request, "tutor_me/view_student_profile.html", {'student': student})


def personal_profile_page(request):
    user_email = SocialAccount.objects.filter(user=request.user)[0].extra_data['email']
    user = CustomUser.objects.filter(email=user_email).get()
    if user.tutor:
        print(user.picture)
        sessions = Session.objects.filter(tutor=user)
        return render(request, "tutor_me/tutor_profile.html", {'tutor': user, 'tutor_sessions': sessions})
    else:
        print(user.picture)
        return render(request, "tutor_me/student_profile.html", {'student': user})

def delete_account(request):
    user_email = SocialAccount.objects.filter(user=request.user)[0].extra_data['email']
    user = CustomUser.objects.filter(email=user_email).get()
    print("DELETED")
    user.delete()
    return(redirect("/"))

def notification_history(request):
    user_email = SocialAccount.objects.filter(user=request.user)[0].extra_data['email']
    user = CustomUser.objects.filter(email=user_email).get()
    if user.tutor:
      past_notifications = Notification.objects.filter(tutor=user, read=True).order_by("-created_at")
    else:
      past_notifications = Notification.objects.filter(student=user, read=True).order_by("-created_at")
    return render(request, "tutor_me/notification_history.html", {'past_notifications': past_notifications})
