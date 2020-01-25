from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import UserForm
# from .serializers import UserSerializer
import json


class UserData(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        data = {'username': user.username, 'is_admin': user.is_superuser}
        return Response(data)


@api_view(['GET', 'POST'])
def register(request):

    if request.method == 'POST':
        login = request.data['username']
        to_email = request.data['email']
        password = request.data['password']
        user_data = {'username': login, 'email': to_email, 'password': password}

        form = UserForm(user_data)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(password)
            user.is_active=False
            user.save()

            # current_site = get_current_site(request)
            message = '127.0.0.1:8080' + '/email/?code=' + urlsafe_base64_encode(force_bytes(user.pk))
            subject = 'Activate your account'
            email = EmailMessage(subject, message, to=[request.data['email']])
            email.send()

            return Response({'valid':'yes'})
        else:
            return Response(form.errors)


@api_view(['GET', 'POST'])
def activate(request):
    if request.method == 'POST':
        try:
            data = request.data['user_id']
            user_id = force_text(urlsafe_base64_decode(data))
            user = User.objects.get(pk=user_id)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist) as error:
            user = None
        if user is not None:
            user.is_active = True
            user.save()
            return Response({'res':'yes'})
        else:
            return Response({'res':'no'})
