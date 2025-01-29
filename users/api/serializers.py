from uuid import uuid4
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.core.validators import MinLengthValidator
from django.conf import settings
from django.contrib.auth.hashers import  check_password

from random import randint

from rest_framework import serializers
   
from users.models import User 




class SingUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required = True)
    password = serializers.CharField(write_only = True , validators=[MinLengthValidator(8)] , required = True)
    confirm_password = serializers.CharField(required = True , write_only = True)
    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'detail':'the passwords do not match'})
        email_user = User.objects.filter(email = attrs['email']).first()
        if email_user :
            raise serializers.ValidationError({'detail':'this email is existed'})
        return super().validate(attrs)
    
    def create(self, validated_data):
        
        validated_data.pop('confirm_password')
        validated_data['is_active'] = False
        validated_data['activation_code'] = randint(1000,9999)

        send_mail(
            f"Activation Code ",
            f"welcome {validated_data['username']}\n Here is the activation code : {validated_data['activation_code']}.",
            settings.EMAIL_HOST_USER,
            {validated_data['email']},
            fail_silently=False,
        )
        user = User.objects.create_user(**validated_data)
        return {}
    


class UserActivateSerializers(serializers.Serializer):
    code = serializers.CharField(required=True , write_only=True , )

    def create(self, validated_data):
        user_id = self.context['view'].kwargs['pk']
        user = User.objects.get(id=user_id)
        if user.activation_code != validated_data['code']:
            raise serializers.ValidationError({'detail':'invalid Code'})
        user.is_active = True
        user.activation_code = ''
        user.save()
        return {}
    
class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required = True)
    new_password = serializers.CharField(required = True , write_only = True , validators=[MinLengthValidator(8)])
    confirm_new_password = serializers.CharField(required = True , write_only = True)

    def create(self, validated_data):
        user = self.context['request'].user

        if not check_password(validated_data['password'] , user.password ):
            raise serializers.ValidationError({'detail':'old password not equal password'})
        
        if validated_data['new_password'] != validated_data['confirm_new_password']:
            raise serializers.ValidationError({'message':'The New Passwords do not match.'})
        
        user.set_password(validated_data['new_password'])
        user.save()

        return {}


    def to_representation(self, instance):
        return {'message': 'Password change process completed.'}


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(required = True)

    def create(self, validated_data):
        user = User.objects.filter(email = validated_data['email']).first()
        if not user:
            raise serializers.ValidationError({'detail':'not found'})
        send_mail(
            f"Activation Code ",
            f"welcome {user.username}\n Here is the activation code : http://127.0.0.1:8000/api/user/reset-password-activat.",
            settings.EMAIL_HOST_USER,
            {validated_data['email']},
            fail_silently=False,
        )
        return {}