from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

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
                messages.info(request,'User name already exists...')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists...')
                return redirect('register')
            else:
                user = User.objects.create_user(username= username, first_name= firstname, last_name=lastname, password= password1,email=email)
                user.save()
                messages.info(request,'user created')
                return redirect('register')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')