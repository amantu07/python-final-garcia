from django.forms import ModelForm
from .models import *

class CommentForm(ModelForm):
    class Meta:
        model = Comentarios
        fields = ('nombre', 'email', 'comentario')

class ContactForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('titulo','contenido')