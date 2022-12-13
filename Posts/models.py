from django.db import models

class Categoria(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title 

class Autor(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria,on_delete=models.SET_NULL, null=True)
    autor = models.ForeignKey(Autor,on_delete=models.SET_NULL, null=True)
    destacado = models.BooleanField(default=False)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return self.titulo

class Comentarios(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name= 'comments')
    nombre = models.CharField(max_length=40)
    email = models.EmailField(default=None)
    fecha = models.DateTimeField(auto_now_add=True)    
    comentario = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return f'Comentario de {self.nombre} - {self.comentario}'


class Contacto(models.Model):
        nombre = models.CharField(max_length=40)
        telefono = models.IntegerField()
        email = models.EmailField(default=None)
        comentario = models.TextField()
        def __str__(self):
            return f'Contacto de de {self.nombre} - {self.comentario}'