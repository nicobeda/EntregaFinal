
from django.urls import path
from Distri import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('cat/', views.catalogo, name="catalogo"),
    path('ini/', views.inicio, name="inicio"),
    path('about/', views.aboutme, name="about"),
    path('sign/', views.signup, name="sign"),
    path('log/', views.log, name="log"),
    path('logout/', LogoutView.as_view(template_name='Distri/inicio.html'), name='logout'), 
    path('cata/', views.leches, name = "lecheee")
]
