from django.urls import path

from loto.loto_auth.views import register_user, login_user, logout_user, update_user, change_password

urlpatterns = (
    path('register/', register_user, name='register user'),
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('update/', update_user, name='update user'),
    path('password/', change_password, name='change password'),
)