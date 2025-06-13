from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("", views.home, name="home"),
    path("apropos/", views.apropos, name="apropos"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path("profile/<slug:slug>/", views.profile, name="profile"),
    path('change-profile-image/', views.change_profile_image, name='change_profile_image'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('delete-profile-image/', views.delete_profile_image, name='delete_profile_image'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('profiles/<slug:slug>/', views.profile_details, name='profile_details'),
    path('historique-connexion/', views.historique_connexion, name='historique_connexion'),
    path('user-list/', views.user_list, name='user_list'),
    path("logout/", views.logout_view, name="logout"),

]