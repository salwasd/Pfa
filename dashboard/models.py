from django.db import models
from django.contrib.auth.models import User

class Utilisateur(models.Model):
    CLIENT = 'client'
    AUTHORITAIRE = 'authoritaire'
    ADMIN = 'Admin'

    ROLE_CHOICES = (
        (CLIENT, 'client'),
        (AUTHORITAIRE, 'authoritaire'),
        (ADMIN, 'Admin'),
    )
    User = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    ID = models.CharField(max_length=100, primary_key=True)
    Nom = models.CharField(max_length=100)
    Prenom = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Cin = models.CharField(max_length=100)
    Role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    def __str__(self):
        return f"{self.Nom} {self.Prenom}"

