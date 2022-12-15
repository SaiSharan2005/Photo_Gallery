from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from . models import *
from .forms import *
# Create your views here.


def loginPage(request):
    task = 'login'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {'task': task}
    return render(request, "show_photo/login_registration.html", context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def createUser(request):
    task = ''
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'task': task, 'form': form}
    return render(request, "show_photo/login_registration.html", context)


def home(request):
    rooms = Room.objects.all()
    user = User.objects.all()
    context = {'rooms': rooms, 'user': user}
    return render(request, "show_photo/home.html", context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    room = user.room_set.all()
    context = {'user': user, 'rooms': room}
    return render(request, 'show_photo/profile.html', context)


def image_view(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        Messages.objects.create(
            host=request.user,
            room = room,
            message=request.POST.get('comment')
            )
        return redirect('home')
    messages = room.messages_set.all()
    context = {'room': room,'messages':messages}
    return render(request, "show_photo/image.html", context)

@login_required(login_url='/login')
def upload_photo(request):
    if request.method == 'POST':
        Room.objects.create(
            host=request.user,
            image=request.FILES.get('image'),
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')

    form = RoomForm()
    context = {'form': form}
    return render(request, 'show_photo/upload_photo.html', context)

@login_required(login_url='/login')
def update_photo(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.user == room.host:
        if request.method == 'POST':
            room.host = request.user
        # room.image=request.FILES.get('image'),
            room.name = request.POST.get('name')
            room.description = request.POST.get('description')
            room.save()
            return redirect('home')
    else:
        return HttpResponse("You are not allowed to do the task")
    context = {'form': form,'room':room}
    return render(request, 'show_photo/update_photo.html', context)


@login_required(login_url='/login')
def delete_photo(request, pk):
    room = Room.objects.get(id=pk)
    if request.user == room.host:
        room.delete()
        return redirect('home')
    else:
        return HttpResponse("You are not allowed to do the task")


@login_required(login_url='/login')
def update_comment(request, pk):
    term = "Message"
    messages = Messages.objects.get(id=pk)
    form = MessagesForm(instance=messages)
    if request.user == messages.host:
        if request.method == 'POST':
            messages.host = request.user
            messages.room = messages.room
            messages.message = request.POST.get('comment')
            messages.save()
            return redirect('home')
    else:
        return HttpResponse("You are not allowed to do the task")
    context = {'messages': messages,'term':term}
    return render(request, 'show_photo/update_photo.html', context)

@login_required(login_url='/login')
def delete_comment(request, pk):
    room = Messages.objects.get(id=pk)
    if request.user == room.host:
        room.delete()
        return redirect('home')
    else:
        return HttpResponse("You are not allowed to do the task")
