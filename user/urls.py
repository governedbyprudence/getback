from django.urls import path
from .views import user_view

urlpatterns = [
    path("user_register",user_view,name="register_user")
]
