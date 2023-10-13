from django.urls import path
from .views import CreateUser, LoginUser, logout_user, detail_user

urlpatterns = [
    path('register/', CreateUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('detail_user/', detail_user, name='detail_user')
]