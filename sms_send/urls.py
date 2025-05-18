from django.urls import path
from .views import sms_sender_view

urlpatterns = [
    path('', sms_sender_view, name='sms_sender'),
]
