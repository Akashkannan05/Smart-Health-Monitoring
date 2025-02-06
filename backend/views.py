from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,views,serializers,status
from django.http import JsonResponse
from .models import UserProfileModel
from .serializers import ProfileSerializer


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
            return JsonResponse({"Login":"Not_logined"},status=403)
        data=UserProfileModel.objects.get(User=user)
        serilaize=ProfileSerializer(data)
        return Response(serilaize.data,status=200)
    
ProfileDetailViewClass=ProfileDetailView.as_view()
