from django.urls import path
from .views import list_users, list_agent, list_services, CreateServiceView

urlpatterns = [
    path('users/', list_users, name='list_users'),
    path('bodyguards/', list_agent, name='list_bodyguards'),
    path('services/', list_services, name='list_services'),
    path('services/create/', CreateServiceView.as_view(), name='create_service'),
]