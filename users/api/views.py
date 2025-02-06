from django.shortcuts import render

from rest_framework import mixins , viewsets , status , serializers
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny

from .serializers import SingUpSerializer , UserActivateSerializers , ChangePasswordSerializer , ResetPasswordSerializer , ConfirmResetPasswordSerializer , ProfileDoctorAndNurseSerializer ,PatientProfileSerializer
from users.models import User , DoctorNurseProfile ,PatientProfile


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
    
    @action(detail=False , methods=['post'] , serializer_class = ResetPasswordSerializer)
    def reset_password(self,*args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data = data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({'detail':'check message on mail'})
    
    @action(
        detail=False ,
        methods=['post'] ,
        serializer_class = ConfirmResetPasswordSerializer , 
        url_path=r'confirm-reset-password/(?P<token>\d+)'
    )
    def confirm_reset_password(self,*args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data = data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({'detail':'password change successfully'})
    
class UserProfile(viewsets.GenericViewSet):
    queryset = DoctorNurseProfile.objects.all()
    serializer_class = ProfileDoctorAndNurseSerializer

    @action(detail=True , methods=['get'])
    def doctor(self,*args, **kwargs):
        pk = self.kwargs['pk']
        doctor_or_nurse = DoctorNurseProfile.objects.filter(id = pk).first()

        if not doctor_or_nurse:
            raise serializers.ValidationError({'error':'doctor not found'})
        
        serializer = self.get_serializer(doctor_or_nurse)
        return Response(serializer.data)
    
    @action(detail = True , methods=['get'] , serializer_class = PatientProfileSerializer)
    def Patient(self ,*args, **kwargs):
        pk = self.kwargs['pk']
        Patient = PatientProfile.objects.filter(id = pk).first()

        if not Patient:
            raise serializers.ValidationError({'error':'Patient not found'})
        
        serializer = self.get_serializer(Patient)
        return Response(serializer.data)
