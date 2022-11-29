from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField()
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    def __str__(self):
        return self.titulo


class Comentarios(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name= 'comments')
    nombre = models.CharField(max_length=40)
    email = models.EmailField(default=None)
    fecha = models.DateTimeField(auto_now_add=True)    
    comentario = models.TextField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return f'Comentario de {self.nombre} - {self.comentario}'


class Contacto(models.Model):
        nombre = models.CharField(max_length=40)
        telefono = models.IntegerField()
        email = models.EmailField(default=None)
        comentario = models.TextField()
        def __str__(self):
            return f'Contacto de de {self.nombre} - {self.comentario}'
