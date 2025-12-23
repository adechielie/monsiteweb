from django.urls import path
from .views import predictions_view

urlpatterns = [
    path('', views.predictions, name="prediction"),
    ]