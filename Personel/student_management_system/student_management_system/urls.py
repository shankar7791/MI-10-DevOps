
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from student_management_app import HodViews, views, StudentViews

urlpatterns = [
    path('signup_admin',views.signup_admin,name="signup_admin"),
    path('signup_student',views.signup_student,name="signup_student"),
    path('do_admin_signup',views.do_admin_signup,name="do_admin_signup"),
    path('do_student_signup',views.do_student_signup,name="do_student_signup"),
    


    #hod
    path('admin/', admin.site.urls),
    path('',views.ShowLoginPage,name="show_login"),
    path('get_user_details', views.GetUserDetails,name="get_user_details"),
    path('doLogin',views.doLogin,name="do_login"),
    path('logout_user', views.logout_user,name="logout_user"),
    path('admin_home',HodViews.admin_home,name="admin_home"),
    path('add_staff',HodViews.add_staff,name="admin_home"),
    path('add_staff_save',HodViews.add_staff_save,name="add_staff_save"),
    path('add_course',HodViews.add_course,name="add_course"),
    path('add_course_save',HodViews.add_course_save,name="add_course_save"), 
    path('add_student',HodViews.add_student,name="add_student"), 
    path('add_student_save',HodViews.add_student_save,name="add_student_save"), 
    path('manage_student',HodViews.manage_student,name="manage_student"),
    path('manage_course',HodViews.manage_course,name="manage_course"),
    path('edit_student/<str:student_id>',HodViews.edit_student,name="edit_student"),
    path('edit_student_save',HodViews.edit_student_save,name="edit_student_save"),
    path('delete_student/<student_id>/', HodViews.delete_student, name="delete_student"),
    path('view_profile/<str:student_id>',HodViews.view_profile,name="view_profile"),

    path('edit_student_profile/<str:student_id>',HodViews.edit_student_profile),
    path('edit_student_save_profile',HodViews.edit_student_save_profile),

    path('edit_course/<str:course_id>',HodViews.edit_course,name="edit_course"),
    path('edit_course_save',HodViews.edit_course_save,name="edit_course_save"),

    

    

    # student url
    path('student_home',StudentViews.student_home,name="student_home"),
    path('student_profile',StudentViews.student_profile,name="student_profile"),
    path('student_profile_save',StudentViews.student_profile_save,name="student_profile_save"),




]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
