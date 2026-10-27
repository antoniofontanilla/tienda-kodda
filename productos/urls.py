from django.urls import path
from . import views

urlpatterns = [
    # 🌟 Ruta Principal / Catálogo Comercial Público
    path('', views.catalogo, name='catalogo'),

    # 🛠️ Rutas del Panel Admin de Productos (Protegidas)
    path('admin-panel/productos/', views.lista_productos, name='lista_productos'),
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),

    # 📁 Rutas de Categorías (Panel Admin)
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/nueva/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', views.eliminar_categoria, name='eliminar_categoria'),
]