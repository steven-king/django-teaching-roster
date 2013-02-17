#!/usr/bin/env python

from django.contrib import admin
from roster.models import Course, Student



class CourseAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    
admin.site.register(Course, CourseAdmin)

class StudentAdmin(admin.ModelAdmin):
    search_fields = ('name',),


admin.site.register(Student, StudentAdmin)

