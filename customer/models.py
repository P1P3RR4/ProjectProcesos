from django.db import models

class MenuItem(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.nombre
    
class Category(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class ModeloOrden(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField(
        'MenuItem', related_name='order', blank=True)

    def __str__(self):
        return f'order: {self.created_on.strftime("%b %d %I:%M %p")}'