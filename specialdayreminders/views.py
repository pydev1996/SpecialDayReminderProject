# SpecialDayReminderProject/specialdayreminders/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import SpecialDayReminder
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FCMToken
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FCMToken
from django.contrib.auth.decorators import login_required

@api_view(['POST'])
@login_required
def save_fcm_token(request):
    user = request.user
    token = request.data.get('token')

    if token:
        # Save the FCM token in the database
        FCMToken.objects.update_or_create(user=user, defaults={'token': token})
        return Response({'message': 'Token saved successfully'}, status=201)
    else:
        return Response({'message': 'Token not provided'}, status=400)



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
from datetime import timedelta
from django.shortcuts import render
from django.utils import timezone
from .models import SpecialDayReminder
from .firebase_utils import send_fcm_notification  # This is a custom function for sending FCM notifications
from django.views.decorators.csrf import csrf_exempt
@login_required
@csrf_exempt
def special_day_reminder_list(request):
    reminders = SpecialDayReminder.objects.filter(user=request.user)
    if request.method == 'POST':
        fcm_token = request.POST.get('token')

        

        for reminder in reminders:
            time_difference = reminder.date - timezone.localtime().date()
            #print(fcm_token)
            if time_difference == timedelta(days=1):
                title = "Special Day Reminder"
                message = f"Tomorrow is {reminder.name}'s ({reminder.specialday_type}) day. Please wish them!"
                #print(message)
                send_fcm_notification(fcm_token, title, message)
                break

        return render(request, 'special_day_reminder_list.html', {'reminders': reminders})

    else:
       

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

from django.http import HttpResponse

def firebase_messaging_sw(request):
    # Assuming you have the 'firebase-messaging-sw.js' file in your static files directory
    file_path = 'C:/Users/dell/Downloads/SpecialDayReminderProject/specialdayreminders/templates/firebase-messaging-sw.js'

    # Read the contents of the 'firebase-messaging-sw.js' file
    with open(file_path, 'r') as file:
        js_content = file.read()

    # Set the proper MIME type for the response
    response = HttpResponse(js_content, content_type='application/javascript')
    return response







