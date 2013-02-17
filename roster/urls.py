# app urls roster/urls.py
from django.conf.urls.defaults import patterns, url

from roster import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='roster_home'),
    url(r'^course/$', views.courseList, name='roster_course_list'),
    url(r'^student/$', views.studentList, name='roster_student_list'),
    url(r'^course/(?P<pk>\d+)$', views.course, name='roster_course'),
    url(r'^student/(?P<pk>\d+)$', views.student, name='roster_student'),
    )

