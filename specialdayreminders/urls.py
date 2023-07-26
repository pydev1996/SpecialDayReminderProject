# SpecialDayReminderProject/specialdayreminders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('firebase-messaging-sw.js', views.firebase_messaging_sw, name='firebase_messaging_sw'),
    path('specaildaylist/', views.special_day_reminder_list, name='special_day_reminder_list'),
    path('add/', views.add_special_day_reminder, name='add_special_day_reminder'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),  # Add logout URL
    path('api/save-fcm-token/', views.save_fcm_token, name='save_fcm_token'),
]

