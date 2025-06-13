from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur, HistoriqueConnexion
from django.utils.html import format_html

class UtilisateurAdmin(UserAdmin):
    # Champs à afficher dans la liste des utilisateurs
    list_display = ('username', 'email', 'first_name', 'last_name', 'telephone', 'date_naissance', 'bio', 'genre', 'slug', 'profile_link_display', 'reseaux_sociaux_display', 'is_staff')
    
    def profile_link_display(self, obj):
        if obj.profile_link:
            return format_html('<a href="{}" target="_blank">{}</a>', obj.profile_link, obj.profile_link)
        return "Pas de lien"

    profile_link_display.short_description = "Lien du profil"

    def reseaux_sociaux_display(self, obj):
        if obj.reseaux_sociaux:
            links = []
            for reseau, url in obj.reseaux_sociaux.items():
                links.append(format_html('<a href="{}" target="_blank">{}</a>', url, reseau))
            return format_html(" | ".join(links))
        return "Aucun réseau social"

    reseaux_sociaux_display.short_description = "Réseaux sociaux"

    # Champs à rechercher dans la vue admin
    search_fields = ('username', 'email', 'first_name', 'last_name', 'telephone')

    # Champs affichés lors de la modification ou de la création d'un utilisateur
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {
            'fields': (
                'first_name', 'last_name', 'email', 'bio', 'image', 'cover_image',
                'date_naissance', 'adresse', 'telephone', 'genre', 'reseaux_sociaux'
            )
        }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Champs pour le formulaire d'ajout d'un nouvel utilisateur
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'bio', 
                       'image', 'cover_image', 'telephone', 'date_naissance', 'adresse', 'genre', 'reseaux_sociaux')
        }),
    )

    # Pagination et gestion des utilisateurs dans la vue liste
    ordering = ('username',)

class HistoriqueConnexionAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'date', 'adresse_ip')
    search_fields = ('utilisateur__username', 'adresse_ip')
    list_filter = ('date',)

# Enregistrement des modèles dans l'admin Django
admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(HistoriqueConnexion, HistoriqueConnexionAdmin)
