from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class Utilisateur(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='cover_images/', blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    genre = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')], blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    profile_link = models.URLField(blank=True, null=True)

    # Champ JSON pour stocker plusieurs comptes de réseaux sociaux
    reseaux_sociaux = models.JSONField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        self.profile_link = f"http://127.0.0.1:8000/profiles/{self.slug}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class HistoriqueConnexion(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    adresse_ip = models.GenericIPAddressField()

    def __str__(self):
        return f"Connexion de {self.utilisateur.username} le {self.date}"
