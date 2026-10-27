from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # <--- Importar el decorador
from django.db.models import Q
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm

# ================= VISTAS DE PRODUCTOS =================

@login_required
def lista_productos(request):
    query = request.GET.get('q', '') # Captura lo que el usuario escribió en el buscador
    if query:
        # Filtra si el nombre del producto O el nombre de su categoría contienen el texto buscado
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) | Q(categoria__nombre__icontains=query)
        )
    else:
        productos = Producto.objects.all()
        
    return render(request, 'productos/lista_productos.html', {'productos': productos, 'query': query})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/form_producto.html', {'form': form})

@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/form_producto.html', {'form': form})

@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/confirmar_eliminacion.html', {'objeto': producto, 'tipo': 'producto'})


# ================= VISTAS DE CATEGORÍAS =================

@login_required
def lista_categorias(request):
    query = request.GET.get('q', '') # Captura el texto de búsqueda para categorías
    if query:
        categorias = Categoria.objects.filter(nombre__icontains=query)
    else:
        categorias = Categoria.objects.all()
        
    return render(request, 'productos/lista_categorias.html', {'categorias': categorias, 'query': query})

@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'productos/form_categoria.html', {'form': form})

@login_required
def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'productos/form_categoria.html', {'form': form})

@login_required
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'productos/confirmar_eliminacion.html', {'objeto': categoria, 'tipo': 'categoría'})

# ================= VISTA PÚBLICA / CATÁLOGO =================

def catalogo(request):
    query = request.GET.get('q', '')
    categoria_id = request.GET.get('categoria', '')
    
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    
    # Filtro por búsqueda de texto
    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) | Q(categoria__nombre__icontains=query)
        )
        
    # Filtro por categoría seleccionada
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
        
    context = {
        'productos': productos,
        'categorias': categorias,
        'query': query,
        'categoria_seleccionada': int(categoria_id) if categoria_id.isdigit() else None,
    }
    return render(request, 'productos/catalogo.html', context)