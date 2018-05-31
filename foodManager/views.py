from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Inventario
from .forms import InventarioForm

# Create your views here.

def productos_list (request):
    inventarios = Inventario.objects.order_by('cantidadActual')
    return render(request, 'foodManager/productos_list.html', {'inventarios': inventarios})

def consumir_producto (request,pk):
    producto = get_object_or_404(Producto, nombre=pk)
    inventario = get_object_or_404(Inventario, producto=producto.pk)

    if request.method == "POST":
        form = InventarioForm(request.POST, instance=inventario)
        if form.is_valid():
            inventario = form.save(commit=False)
            inventario.cantidadActual -= int(request.POST.get("cantidad"))
            inventario.stock += 1
            inventario.save()
            return redirect('main')
    else:
        form = InventarioForm(instance=inventario)
    return render(request, 'foodManager/consumir.html', {'inventario': inventario, 'form': form})