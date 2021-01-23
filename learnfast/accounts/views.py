from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import  login, authenticate



from .forms import RegisterForm


def register(request):
    template_name = "accounts/register.html"
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_user = authenticate(request, username=user.username, password=form.cleaned_data['password1'])
            login(request, auth_user)
            return redirect('home')
    else:
        form = RegisterForm()
    context = {'form': form}

    return render(request, template_name, context)



def areaDoAluno(request):
    template_name = 'student_area/index.html'

    context = {
        
    }
    return render(request, template_name, context)


