from django.shortcuts import render
from .models import Producto

# Create your views here.

def productos_list (request):
    productos = Producto.objects.order_by('nombre')
    return render(request, 'foodManager/productos_list.html', {'productos': productos})
