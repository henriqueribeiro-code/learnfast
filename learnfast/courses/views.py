from django.shortcuts import render, get_object_or_404

from .models import Courses
from .forms import ContactCourseForms


def index(request):
    courses = Courses.objects.all()
    template_name = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)


def course_details(request, slug):
    course =  get_object_or_404(Courses, slug=slug)
    context = {}
    if request.method == "POST":
        form = ContactCourseForms(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            print(form.cleaned_data)
            form = ContactCourseForms()
    else:
        form = ContactCourseForms()
    context['form'] = form
    context['course'] = course
    template_name = 'courses/course.html'
    return render(request, template_name, context)