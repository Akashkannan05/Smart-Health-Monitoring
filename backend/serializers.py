from rest_framework import serializers
from .models import UserProfileModel


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserProfileModel
        fields=[
           'MedicalID',
           'User',
           'DateOfBirth',
           'Gender',
           'Age',
           'PhoneNumber',
           'Address',
           'Country',
           'MedicalRecord',
           'QRCode',
           'ProfilePic'
        ]
    