from django.urls import path
from . import views
urlpatterns=[
    path('',views.Home.as_view()),
    path('profile/',views.ProfileDetailViewClass,name="Profile page"),
    path('login/',views.LoginViewClass,name="Login")
]