from django.contrib import admin
from  .models import *

class PostAdmin(admin.ModelAdmin):
    fields = ('titulo','slug','contenido')

    prepopulated_fields = {'slug':('titulo',)}

admin.site.register(Post,PostAdmin)

admin.site.register(Comentarios)

admin.site.register(Contacto)
