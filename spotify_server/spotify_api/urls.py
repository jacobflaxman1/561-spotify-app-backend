from django.urls import path
from .views import AuthUrl

urlpatterns = [
    path('/get-auth-url', AuthUrl.as_view()),
]