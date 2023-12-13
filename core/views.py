from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
# Create your views here.

@login_required(login_url='sign_in')
def index(request):
  return render(request, 'index.html')

def sign_up(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    pass_confirm = request.POST['pass_confirm']
    if password != pass_confirm:
      messages.info(request, "Passwords doesn't match")
      return redirect('sign_up')
    if User.objects.filter(username=username).exists():
      messages.info(request, 'Username taken')
      return redirect('sign_up')
    if User.objects.filter(email=email):
      messages.info(request, 'Email already exists')
      return redirect('sign_up')
    new_user = User.objects.create_user(username=username, email=email, password=password)
    new_user.save()
    
    #create profile model
    user = User.objects.get(username=username)
    new_profile = Profile.objects.create(user=user, id_user=user.id)
    new_profile.save()
  
  return render(request, 'signup.html')

def sign_in(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    
    user = auth.authenticate(username=username, password=password)
    
    if user:
      auth.login(request, user)
      return redirect('/')
    messages.info(request, 'Credentials invalid')
    return redirect('sign_in')
  return render(request, 'signin.html')

@login_required(login_url='sign_in')
def logout(request):
  auth.logout(request)
  return redirect('sign_in')


