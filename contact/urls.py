from django.urls import path
from .views import contact_view, contact_succes

urlpatterns = [
    path('', contact_view, name='contact'),
    path('succes/', contact_succes, name='contact_succes'),
]