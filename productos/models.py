from django.db import models

# Modelo para las Categorías
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Categoría")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre

# Modelo para los Productos
class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Producto")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    descripcion = models.TextField(blank=True, null=True)
    stock = models.IntegerField(verbose_name="Stock disponible")
    # Relación: Un producto pertenece a una sola categoría (ForeignKey)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True, verbose_name="Imagen")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"