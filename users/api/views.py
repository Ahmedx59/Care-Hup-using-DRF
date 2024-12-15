from django.shortcuts import render

from rest_framework import mixins , viewsets
from rest_framework.decorators import action
from rest_framework.response import Response 


from users.models import User
from .serializers import AuthSerializer


# class AuthUser(
#     viewsets.GenericViewSet):

#     queryset = User.objects.all()
#     serializer_class = AuthSerializer

#     @action(detail=True , methods=['post'])
#     def create(self,*args, **kwargs):
#         data = self.request.data
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return {}