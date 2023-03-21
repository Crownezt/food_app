from django.db import models
from django.urls import reverse


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_at, self.name

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
