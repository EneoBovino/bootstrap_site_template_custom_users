from django.urls import path
from usuarios.views import login, register, logout

urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]