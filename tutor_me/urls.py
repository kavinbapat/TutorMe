from django.urls import path
from django.contrib.auth.views import LogoutView
from tutor_me import views

app_name="tutor_me"
urlpatterns = [
    path('', views.index_view, name="index"),
    path('logout', LogoutView.as_view(), name="logout"),
    path("register/", views.register_request, name="register"),
    path("direct/", views.direct_user, name="direct"),
    path("direct/accept/<int:id>", views.accept_session, name="accept_request"),
    path("direct/decline/<int:id>", views.decline_session, name="decline_request"),
    path("direct/student_cancel_session/<int:id>", views.student_cancel_session, name="student_cancel_session"),
    path("direct/tutor_cancel_session/<int:id>", views.tutor_cancel_session, name="tutor_cancel_session"),
    path("departments/", views.getAllDepartments, name="departments"),
    path("courses/<str:course_subject>", views.getAllCoursesFromDepartment, name="courses"),
    path("courses/<path:course>/interact", views.CourseInteract, name="courseinteract"),
    path("departments/search/", views.DepartmentSearch, name="search_results"),
    path("courses/<str:course_subject>/search/", views.CourseSearch, name="search_course"),
    path("interact/<int:id>", views.request_session, name="request_session"),
    path("direct/view_tutor_profile_page/<int:id>", views.view_tutor_profile_page, name="tutor_profile_page"),
    path("direct/view_student_profile_page/<int:id>", views.view_student_profile_page, name="student_profile_page"),
    path("direct/personal_profile_page/", views.personal_profile_page, name="personal_profile_page"),
    path("direct/tutor_cancel_notification/<int:id>",views.tutor_cancel_notification, name="tutor_cancel_notification"),
    path("direct/student_cancel_notification/<int:id>",views.student_cancel_notification, name="student_cancel_notification"),
    path("personal_profile_page/delete_account", views.delete_account, name="delete_account"),
    path("direct/notification_history",views.notification_history,name="notification_history")
]
