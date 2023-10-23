
from django.urls import path
from Distri import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('cati/', views.catalogo, name="agreg"),
    path('ini/', views.inicio, name="inicio"),
    path('about/', views.aboutme, name="about"),
    path('sign/', views.signup, name="sign"),
    path('log/', views.log, name="log"),
    path('logout/', LogoutView.as_view(template_name='Distri/inicio.html'), name='logout'), 
    path('cat/', views.leches, name = "catalogo"),
    path('cat2/', views.galles, name = "catalogo2"),
    path('cato/', views.agregalle, name = "agregalle"),
]
