from django.shortcuts import render

from rest_framework import mixins , viewsets
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny

from .serializers import AuthSerializer , UserActivateSerializers
from users.models import User


class AuthUser(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = AuthSerializer


    def get_permissions(self):
        if self.action  in ['create','activate']:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'create':
            return AuthSerializer
        return super().get_serializer_class()
    
    
    # # @action(detail=True , methods=['post'])
    # def create(self,*args, **kwargs):
    #     data = self.request.data
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception = True)
    #     serializer.save()
    #     return Response({"detail": "User created successfully.", "user": serializer.data})
    

        
    @action(detail=True , methods=['post'] , serializer_class=UserActivateSerializers)
    def activate(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception =True)
        serializer.save()
        return Response ({'detail':'your account created successfully'})
  