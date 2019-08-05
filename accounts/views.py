from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from events.models import Event
from event_types.models import EventType
from counties.models import County
from categories.models import Category

def register(request):
    #handles user registration
    if request.method == 'POST':
      # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        # subscribe = request.POST['subscribe']

        # Check if passwords match
        if password == confirm_password:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
              # Check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                  # Looks good
                    user = User.objects.create_user( username=username, password=password,email=email, first_name=first_name, last_name=last_name)
                    # Login after register and be redirected to index page
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
          messages.error(request, 'Passwords do not match')
          return redirect('register')
    else:
      return render(request, 'pages/auth/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
      return render(request, 'pages/auth/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')

def dashboard(request):
    counties = County.objects.all()
    trending = Event.objects.all().order_by('-event_date').filter(event_type='1')
    featured = Event.objects.all().order_by('-event_date').filter(event_type='2')
    tonight = Event.objects.all().order_by('-event_date').filter(event_type='3')
    this_weekend = Event.objects.all().order_by('-event_date').filter(event_type='4')


    context = {
        "counties" : counties,
        "trending" : trending,
        "featured" : featured,
        "tonight" : tonight,
        "this_weekend" : this_weekend
    }
    return render(request, 'pages/auth/dashboard.html', context)
