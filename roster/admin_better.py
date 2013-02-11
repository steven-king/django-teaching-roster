#!/usr/bin/env python

from django.contrib import admin
from roster.models import Course, Student


class MembershipInline(admin.TabularInline):
    model = Course


class CourseAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    inlines = [
        MembershipInline,
    ]

admin.site.register(Course, CourseAdmin)

class StudentAdmin(admin.ModelAdmin):
    search_fields = ('name',),
    inlines = [
        MembershipInline,
    ]



admin.site.register(Student, StudentAdmin)

