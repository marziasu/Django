
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,HOD_views, Stuff_Views, Student_Views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),

    # login path
    path('', views.LOGIN, name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),

    # profile update
    path('profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE,name='profile_update'),

    # hod panel url
    path('HOD/home',HOD_views.HOME,name='hod_home'),
    path('HOD/Student/Add',HOD_views.ADD_STUDENT,name='add_student'),
    path('HOD/Student/View',HOD_views.VIEW_STUDENT,name='view_student'),
    path('HOD/Student/Edit/<str:id>',HOD_views.EDIT_STUDENT,name='edit_student'),
    path('HOD/Student/Update',HOD_views.UPDATE_STUDENT,name='update_student'),
    path('HOD/Student/Delete/<str:admin>',HOD_views.DELETE_STUDENT,name='delete_student'),

    path('HOD/Department/Add',HOD_views.ADD_DEPARTMENT,name='add_department'),
    path('HOD/Department/View',HOD_views.VIEW_DEPARTMENT,name='view_department'),
    path('HOD/Department/Edit/<str:id>',HOD_views.EDIT_DEPARTMENT,name='edit_department'),
    path('HOD/Department/Update',HOD_views.UPDATE_DEPARTMENT,name='update_department'),
    path('HOD/Department/Delete/<str:id>',HOD_views.DELETE_DEPARTMENT,name='delete_department'),

    path('HOD/Session/Add',HOD_views.ADD_SESSION,name='add_session'),
    path('HOD/Session/View',HOD_views.VIEW_SESSION,name='view_session'),
    path('HOD/Session/Edit/<str:id>',HOD_views.EDIT_SESSION,name='edit_session'),
    path('HOD/Session/Update',HOD_views.UPDATE_SESSION,name='update_session'),
    path('HOD/Session/Delete/<str:id>',HOD_views.DELETE_SESSION,name='delete_session'),


    path('HOD/Stuff/Add',HOD_views.ADD_STUFF,name='add_stuff'),
    path('HOD/Stuff/View',HOD_views.VIEW_STUFF,name='view_stuff'),
    path('HOD/Stuff/Edit/<str:id>',HOD_views.EDIT_STUFF,name='edit_stuff'),
    path('HOD/Stuff/Update',HOD_views.UPDATE_STUFF,name='update_stuff'),
    path('HOD/Stuff/Delete/<str:admin>',HOD_views.DELETE_STUFF,name='delete_stuff'),

    path('HOD/Course/Add',HOD_views.ADD_COURSE,name='add_course'),
    path('HOD/Course/View',HOD_views.VIEW_COURSE,name='view_course'),
    path('HOD/Course/Edit/<str:id>',HOD_views.EDIT_COURSE,name='edit_course'),
    path('HOD/Course/Update',HOD_views.UPDATE_COURSE,name='update_course'),
    path('HOD/Course/Delete/<str:id>',HOD_views.DELETE_COURSE,name='delete_course'),

    path('HOD/Stuff/Send_Notification',HOD_views.STUFF_SEND_NOTIFICATION,name='stuff_send_notification'),
    path('HOD/Stuff/Save_Notification',HOD_views.SAVE_STUFF_NOTIFICATION,name='save_stuff_notification'),
    path('HOD/Stuff/Leave_View',HOD_views.STUFF_LEAVE_VIEW,name='stuff_leave_view'),
    path('HOD/Stuff/Leave_Message_View/<str:id>',HOD_views.LEAVE_MESSAGE_VIEW,name='leave_message_view'),
    path('HOD/Stuff/Approve_Leave/<str:id>',HOD_views.APPROVE_LEAVE,name='approve_leave'),
    path('HOD/Stuff/Dispprove_Leave/<str:id>',HOD_views.DISAPPROVE_LEAVE,name='disapprove_leave'),
    path('HOD/Stuff/Feedback',HOD_views.STAFF_FEEDBACK,name='staff_feedback'),
    path('HOD/Stuff/Feedback/Save',HOD_views.STAFF_FEEDBACK_SAVE,name='staff_feedback_save'),

    path('HOD/Student/Send_Notification',HOD_views.STUDENT_SEND_NOTIFICATION,name='student_send_notification'),
    path('HOD/Student/Save_Notification',HOD_views.SAVE_STUDENT_NOTIFICATION,name='save_student_notification'),


    # This is Stuff urls
    path('Stuff/Home',Stuff_Views.HOME,name='stuff_home'),
    path('Stuff/Notifications',Stuff_Views.NOTIFICATIONS,name='notifications'),
    path('Stuff/Mark_as_done/<str:status>',Stuff_Views.MARK_AS_DONE,name='mark_as_done'),
    path('Stuff/Apply_Leave',Stuff_Views.STUFF_APPLY_LEAVE,name='stuff_apply_leave'),
    path('Stuff/Apply_Leave_Save',Stuff_Views.STUFF_APPLY_LEAVE_SAVE,name='stuff_apply_leave_save'),
    path('Stuff/Feedback',Stuff_Views.STUFF_FEEDBACK,name='stuff_feedback'),
    path('Stuff/Feedback/Save',Stuff_Views.FEEDBACK_SAVE,name='feedback_save'),
    path('Stuff/Add/Result',Stuff_Views.ADD_RESULT,name='add_result'),
    path('Staff/Save/Result',Stuff_Views.SAVE_RESULT,name='save_result'),
    path('Staff/View/Result',Stuff_Views.STUFF_VIEW_RESULT,name='stuff_view_result'),
    path('Staff/Take_Attendance',Stuff_Views.STUFF_TAKE_ATTENDANCE,name='staff_take_attendance'),
    path('Staff/Save_Attendance',Stuff_Views.STUFF_SAVE_ATTENDANCE,name='staff_save_attendance'),
    path('Staff/View_Attendance',Stuff_Views.STUFF_VIEW_ATTENDANCE,name='staff_view_attendance'),

    path('Staff/Voice',Stuff_Views.SPEAK,name='speak'),

    # This is Student urls
    path('Student/Home',Student_Views.HOME,name='student_home'),
    path('Student/Notification',Student_Views.STUDENT_RE_NOTIFICATION,name='student_re_notification'),
    path('Student/Mark_as_done/<str:status>',Student_Views.MARK_AS_DONE,name='mark_as_done_by_student'),
    path('Student/View_Result',Student_Views.STUDENT_VIEW_RESULT,name='student_view_result'),
    path('Student/View_Attendance',Student_Views.STUDENT_VIEW_ATTENDANCE,name='student_view_attendance')




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
