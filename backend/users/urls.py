from django.urls import path
from .views import register, activate, UserData
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('getdata/', csrf_exempt(UserData.as_view())),
    path('register/', csrf_exempt(register), name='register'),
    path('activation/', csrf_exempt(activate), name='activate'),
]
