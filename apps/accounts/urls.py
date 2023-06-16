from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('register/author', views.AuthorRegisterAPIView.as_view()),
    path('register/user', views.UserRegisterApiView.as_view()),
    path('token/', obtain_auth_token),
    path('auth/', include('rest_framework.urls'))
]

