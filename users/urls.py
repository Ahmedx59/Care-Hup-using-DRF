from django.urls import path 
from rest_framework.routers import DefaultRouter

from users.api.views import AuthUser , UserProfile

router = DefaultRouter()

router.register('Auth' , AuthUser , basename='Auth-user')
router.register('user' , UserProfile , basename='user')



app_name = 'users'
urlpatterns = router.urls