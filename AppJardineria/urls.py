from django.urls import path
from . import views 

urlpatterns = [
    path('home', views.home, name='home'),
    path('productos', views.productos, name='productos'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
    path('checkout', views.checkout, name='checkout'),
]