from django.shortcuts import render

from rest_framework import mixins , viewsets , status
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny

from .serializers import SingUpSerializer , UserActivateSerializers , ChangePasswordSerializer
from users.models import User


class AuthUser(
    viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = SingUpSerializer


    def get_permissions(self):
        if self.action  in ['create','activate']:
            return [AllowAny()]
        return super().get_permissions()


    @action(detail=False , methods=['post'])
    def sign_up(self,*args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({"detail": "User created successfully."})
    

        
    @action(detail=True , methods=['post'] , serializer_class=UserActivateSerializers)
    def activate(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception =True)
        serializer.save()
        return Response ({'detail':'your account created successfully'},status=status.HTTP_200_OK)
    
    @action(detail=False , methods=['post'] , serializer_class= ChangePasswordSerializer)
    def change_password(self,*args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data = data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({'detail':'your password change successfully'})