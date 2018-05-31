from django.shortcuts import render

# Create your views here.

def productos_list (request):
    return render(request, 'foodManager/productos_list.html', {})