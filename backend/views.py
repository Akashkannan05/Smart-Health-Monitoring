from django.shortcuts import render
from django.contrib.auth import login ,logout,authenticate
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,views,serializers,status
from rest_framework.authtoken.models import Token

from .models import UserProfileModel
from .serializers import ProfileSerializer

import json


# Create your views here.

class Home(APIView):
    def get(self,request):
        return JsonResponse({"Hello":"Content"}) 
    
class ProfileDetailView(generics.RetrieveAPIView):
    queryset=UserProfileModel.objects.all()
    serializer_class=ProfileSerializer

    def get(self, request, *args, **kwargs):
        user=self.request.user
        if user is None or user.is_anonymous:
            return JsonResponse({"Login":"Not_logined"},status=status.HTTP_403_FORBIDDEN)
        data=UserProfileModel.objects.get(User=user)
        serilaize=ProfileSerializer(data)
        return JsonResponse(serilaize.data,status=200)
    
ProfileDetailViewClass=ProfileDetailView.as_view()

class LoginView(views.APIView):

    permission_classes=[]

    def post(self, request, *args, **kwargs):
        # username = request.data.get('username')
        # password = request.data.get('password')
        data=json.loads(request.body)
        username=data.get('username')
        password=data.get('password')

        if not username or not password:
            return JsonResponse({"error": "Username and password are required."},status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                #token = Token.objects.get_or_create(user=user)
                login(request,user)
                # return JsonResponse({"token": token.key}, status=status.HTTP_200_OK)
                return JsonResponse({"Done":"success"},status=status.HTTP_200_OK)
            else:
                return JsonResponse({"error": "User account is inactive."},status=status.HTTP_403_FORBIDDEN,)
        else:
            return JsonResponse({"error": "Invalid username or password."},status=status.HTTP_401_UNAUTHORIZED,)

LoginViewClass=LoginView.as_view()
