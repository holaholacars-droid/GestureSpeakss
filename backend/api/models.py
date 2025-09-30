from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    success_mission = models.IntegerField(default=0)
    failed_mission = models.IntegerField(default=0)
    total_mission = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Agent(User):
    experience_years = models.IntegerField(default=0)
    aadhar_no = models.CharField(max_length=20)
    rating = models.FloatField(default=0.0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Agent - {self.name}"

class Service(models.Model):
    bodyguard = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='services_as_bodyguard')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services_as_user')
    service_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Service by {self.bodyguard.name} for {self.user.name} on {self.service_date}"
