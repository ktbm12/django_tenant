from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
# Create your models here.
class Client(TenantMixin):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
        class Domain(DomainMixin):
            domain = models.CharField(max_length=255, unique=True)
            tenant = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='domains')            