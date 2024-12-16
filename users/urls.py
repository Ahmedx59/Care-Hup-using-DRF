from django.urls import path 
from rest_framework.routers import DefaultRouter

from users.api.views import AuthUser

router = DefaultRouter()

router.register('user' , AuthUser , basename='create-user')



app_name = 'users'

urlpatterns = router.urls