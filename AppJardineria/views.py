from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    return render(request, 'AppJardineria/home.html', context) 

def productos(request):
    context={}
    return render (request, 'AppJardineria/productos.html', context)

def nosotros(request):
    context={}
    return render(request, 'AppJardineria/nosotros.html', context)

def contacto(request):
    context={}
    return render(request, 'AppJardineria/contacto.html', context)

def checkout(request):
    context={}
    return render(request, 'AppJardineria/checkout.html', context)