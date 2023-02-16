from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm


def hoem(request):
    return render(request, 'index.html')


def gramatic(request):
    return render(request, 'grammar.html')


def toppic(request):
    return render(request, 'topic.html')


def lesson(request):
    return render(request, 'video.html')
    

def test(request):
    return render(request, 'test.html')


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request, user)
            email = user.email
            email_body = f'Welcome to our family! 😊\n You have successfully registered! \n We beauty salon DOCTOR BEYLER will be happy to serve you.\n Your beauty is our concern'
            data = {'email_body': email_body, 'to_email': email, 'email_subject':f'Good decision {user}.'}
            # Util.send_email(data)
            return redirect('/')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {
        'form':form,
    })


def login_user(request):
    if request.method == "POST": 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            ...
            messages.success(request, "There Was An Error!")
            return redirect('login')
    else:
        return render(request, 'login.html', {})