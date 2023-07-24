# SpecialDayReminderProject/specialdayreminders/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import SpecialDayReminder
from celery import shared_task
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('special_day_reminder_list')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')

from datetime import timedelta
import requests
from django.utils import timezone
from django.shortcuts import render
from .models import SpecialDayReminder
from django.contrib.auth.decorators import login_required
import pywhatkit

@login_required
def special_day_reminder_list(request):
    
    reminders = SpecialDayReminder.objects.filter(user=request.user)
    API_TOKEN='EAABZC7QqicZAwBACBZBoc0Gsk1GgcChbxEVRspbKZBDJT2iSO8uIBDlbKMlLO5FIFfOjVTPnyreDtwNp8EkawDMQJbZAmRY0aFyRZB01CYbmHQhDKC0KYiBk0AAZBI2pwhsvy2BYvwuL7z7vGifjqXesdVHHEZBRUZBz6ZBtnghgnur87mzG1D4IZBnTUE4H48l4bzfyeWvA1ayMwZDZD'
    for reminder in reminders:
        time_difference = reminder.date - timezone.localtime().date()
        print(timedelta(days=1))
        if time_difference == timedelta(days=1):
            # Replace the following line with your WhatsApp Business API endpoint and token
       
            reminder_message = f"Reminder: {reminder.name} ({reminder.specialday_type}) is tomorrow!"
            create_notification("Wishes", reminder_message)


       

    return render(request, 'special_day_reminder_list.html', {'reminders': reminders})


@login_required
def add_special_day_reminder(request):
    if request.method == 'POST':
        name = request.POST['name']
        specialday_type = request.POST['specialday_type']
        date = request.POST['date']
        reminder = SpecialDayReminder(user=request.user, name=name, specialday_type=specialday_type, date=date)
        reminder.save()
        return redirect('special_day_reminder_list')

    return render(request, 'add_special_day_reminder.html')

# specialdayreminders/tasks.py

from plyer import notification

def create_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,  # If you want to use a custom icon, provide the path here
        timeout=10,     # Notification will be shown for 10 seconds (you can change this value)
    )




