from django.contrib import admin
from  .models import *

class PostAdmin(admin.ModelAdmin):
    fields = ('titulo','contenido', 'categoria','autor','destacado')

admin.site.register(Categoria)

admin.site.register(Autor)

admin.site.register(Post,PostAdmin)

admin.site.register(Comentarios)

admin.site.register(Contacto)
