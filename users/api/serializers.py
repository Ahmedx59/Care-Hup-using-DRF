from rest_framework import serializers
from django.utils.crypto import get_random_string
from .views import AuthUser
from django.core.mail import send_mail

from django.utils.crypto import get_random_string
from django.core.validators import MinLengthValidator
from django.conf import settings
from users.models import User 

# class AuthSerializer(serializers.ModelSerializer):
#     email = serializers.CharField(required = True)
#     password = serializers.CharField(required = True , validator = MinLengthValidator(10))
#     password_confirm = serializers.CharField(write_only=True , required = True)
#     class Meta:
#         model = AuthUser 
#         fields = ('email','username','password','password_confirm')
#         extra_kwargs = {
#             'email':{'required':True},
#             'password':{'required':True , 'validators':[MinLengthValidator(8)] , 'write_only':True}
#         }
        
#     def validate(self, attrs):
#         if attrs['password'] != attrs['password_confirm']:
#             raise serializers.ValidationError({'detail':'not ok'})
#         return super().validate(attrs)
    
#     def create(self, validated_data):
#         validated_data.pop('password_confirm')
#         validated_data['is_active'] = False
#         validated_data['activation_code'] = get_random_string(20)
#         user = User.objects.create_user(**validated_data)
        
#         send_mail(
#             f"Activation Code ",
#             f"welcome {user.username}\n Here is the activation code : {user.activation_code}.",
#             settings.EMAIL_HOST_USER,
#             {user.email},
#             fail_silently=False,
#         )
#         return user