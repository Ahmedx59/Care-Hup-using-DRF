from django.urls import path 
from rest_framework.routers import DefaultRouter

from users.api.views import AuthUser , UserProfile , Doctors ,Nurse

router = DefaultRouter()

router.register('Auth' , AuthUser , basename='Auth-user')
router.register('user' , UserProfile , basename='user')
router.register('doctor' , Doctors , basename='doctor')
router.register('nurse' , Nurse , basename='nurse')



app_name = 'users'
urlpatterns = router.urls