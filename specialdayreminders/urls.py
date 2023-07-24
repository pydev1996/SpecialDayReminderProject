# SpecialDayReminderProject/specialdayreminders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('specaildaylist/', views.special_day_reminder_list, name='special_day_reminder_list'),
    path('add/', views.add_special_day_reminder, name='add_special_day_reminder'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),  # Add logout URL
]
