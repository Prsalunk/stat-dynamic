from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):

    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('User name already exists...')
            elif User.objects.filter(email=email).exists():
                print('Email already exists...')
            else:
                user = User.objects.create_user(username= username, first_name= firstname, last_name=lastname, password= password1,email=email)
                user.save()
                print('user created')
        else:
            print('password not matching')
        return redirect('/')

    else:
        return render(request, 'register.html')