from django.db import models
from django.contrib.auth.models import User



class Utilisateur(models.Model):
    CLIENT = 'client'
    AUTHORITAIRE = 'authoritaire'
    
    is_client = models.BooleanField('Is client', default=False)
    is_authoritaire = models.BooleanField('Is authoritaire', default=False)

    ROLE_CHOICES = (
        (CLIENT, 'client'),
        (AUTHORITAIRE, 'authoritaire'),
        
    )
    
    User = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True, related_name='utilisateur')
    ID = models.CharField(max_length=100, primary_key=True)
    Cin = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default='default_username')
    Nom = models.CharField(max_length=100)
    Prenom = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    files = models.ManyToManyField('UserFile', related_name='utilisateur')
    
    def __str__(self):
        return f"{self.Nom} {self.Prenom}"

class UserFile(models.Model):
    utilisateurs = models.ManyToManyField(Utilisateur, related_name='user_files')


    file = models.FileField(upload_to='user_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    clients = models.ManyToManyField(Utilisateur, related_name='client_files')

    def __str__(self):
        return self.file.name