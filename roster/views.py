# roster/views.py
# Create your views here.
from roster.models import Course, Student
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    context = {
        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
    }
    return render(request, "roster/home.html", context)

def course(request, pk):
    #course = Course.objects.order_by('?')[0]
    course = get_object_or_404(Course, id=pk)
    return render(request, "roster/course.html", {'course': course})

def courseList(request):
    course_list = Course.objects.all()
    paginator = Paginator(course_list, 25)
    page = request.GET.get('page')
    try:
        courses= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        courses = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        courses = paginator.page(paginator.num_pages)

    return render(request, 'roster/course_list.html', {"courses": courses})
   
def student(request, pk):
    #student = Student.objects.order_by('?')[0]
    student = get_object_or_404(Student, id=pk)
    return render(request, "roster/student.html", {'student': student})

def studentList(request):
    #student = Student.objects.order_by('?')[0]
    student_list = Student.objects.all()
    paginator = Paginator(student_list, 25)
    page = request.GET.get('page')
    try:
        students= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)

    return render(request, 'roster/student_list.html', {"students": students})
    
    
    #student = get_object_or_404(Student)
    #return render(request, "roster/student_list.html", {'student': student})

    