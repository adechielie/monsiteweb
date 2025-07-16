from django.urls import path
from .views import home, about
from .views import test_email

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('test-email/', test_email, name='test_email'),
]