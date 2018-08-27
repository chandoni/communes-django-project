from django.urls import path, re_path
from .views import SignUp, get_profile

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('user/<slug:name>', get_profile),
]
