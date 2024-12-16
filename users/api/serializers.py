from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.core.validators import MinLengthValidator
from django.conf import settings

from rest_framework import serializers
   
from users.models import User 
# from users.api.views import AuthUser

class AuthSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required = True)
    password = serializers.CharField(write_only = True , validators=[MinLengthValidator(8)] , required = True)
    confirm_password = serializers.CharField(required = True , write_only = True)
    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'detail':'not successfully'})
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['is_active'] = False
        validated_data['activation_code'] = get_random_string(16)
        user = User.objects.create_user(**validated_data)
    
        send_mail(
            f"Activation Code ",
            f"welcome {user.username}\n Here is the activation code : {user.activation_code}.",
            settings.EMAIL_HOST_USER,
            {user.email},
            fail_silently=False,
        )
        return user
    


class UserActivateSerializers(serializers.Serializer):
    code = serializers.CharField(required=True , write_only=True)

    def create(self, validated_data):
        user_id = self.context['view'].kwargs['pk']
        user = User.objects.get(id=user_id)
        if user.activation_code != validated_data['code']:
            raise serializers.ValidationError({'detail':'invalid Code'})
        user.is_active = True
        user.activation_code = ''
        user.save()
        return {}














    
# class AuthSerializer(serializers.ModelSerializer):
#     email = serializers.CharField(required = True)
#     password = serializers.CharField(required = True , write_only=True , validator = MinLengthValidator(10))
#     password_confirm = serializers.CharField(write_only=True , required = True)
#     class Meta:
#         model = AuthUser 
#         fields = ('email','username','password','password_confirm')
        
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
 