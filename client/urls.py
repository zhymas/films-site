from django.urls import path
from .views import CreateUser, LoginUser

urlpatterns = [
    path('register/', CreateUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login')
]