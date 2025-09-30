from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import User, Agent, Service
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

# List all users
def list_users(request):
    users = User.objects.all()
    users_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    return JsonResponse(users_list, safe=False)

# List all bodyguards
def list_agent(request):
    bodyguards = Agent.objects.all()
    bodyguards_list = [{"id": bodyguard.id, "name": bodyguard.name, "experience_years": bodyguard.experience_years} for bodyguard in bodyguards]
    return JsonResponse(bodyguards_list, safe=False)

# List all services
def list_services(request):
    services = Service.objects.all()
    services_list = [{"id": service.id, "bodyguard": service.bodyguard.name, "user": service.user.name, "service_date": service.service_date, "location": service.location, "description": service.description, "is_completed": service.is_completed} for service in services]
    return JsonResponse(services_list, safe=False)

# Create a new service
@method_decorator(csrf_exempt, name='dispatch')
class CreateServiceView(View):
    def post(self, request):
        data = json.loads(request.body)
        bodyguard = get_object_or_404(Agent, id=data['agent_id'])
        user = get_object_or_404(User, id=data['user_id'])
        service = Service.objects.create(
            bodyguard=bodyguard,
            user=user,
            service_date=data['service_date'],
            location=data['location'],
            description=data['description']
        )
        return JsonResponse({"id": service.id, "message": "Service created successfully"})

# URL patterns
