from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView


def index(request):
    destacados = Post.objects.filter(destacado=True)    
    return render(request, 'index.html', {'destacados':destacados})

def buscar(request):
    busqueda = request.GET.get("buscar")
    if busqueda:
        post= Post.objects.filter(
            Q(titulo__icontains = busqueda) |
            Q(contenido__icontains = busqueda)
        ).distinct
    return render(request, 'resultado.html', {'post':post})
    

def all_post(request):
    post = Post.objects.all()  
    return render(request, 'all_post.html', {'post':post})

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias':categorias})

def autores(request):
    autor = Autor.objects.all()
    return render(request, 'autores.html', {'autores':autor})


def post_detail(request,post_id):
    post = Post.objects.get(id=post_id)

    comentarios = post.comments.filter(active=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post
            new_form.save()
            return HttpResponseRedirect('.')
    else:
        form = CommentForm

    return render(request, 'post_detail.html', {'post':post,'comentarios':comentarios,'form':form})


def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = form
            new_form.save()
            return HttpResponseRedirect('.')
    else:
        form = ContactForm

    return render(request, 'contacto.html', {'form':form})

class NuevoPost(CreateView):
    model = Post
    fields = '__all__' 
    success_url = '../all_post/'

class PostEdit(UpdateView):
    model = Post
    fields= '__all__' 
    success_url= '../all_post/' 

class PostDelete(DeleteView):
    model = Post
    success_url= '../all_post/'

class CommentEdit(UpdateView):
    model = Comentarios
    fields= ['nombre','email','comentario']
    success_url= '../all_post/' 

class CommentDelete(DeleteView):
    model = Comentarios
    success_url= '../all_post/'

class CatEdit(UpdateView):
    model = Categoria
    fields= ['title']
    success_url= '../categorias/' 

class CatDelete(DeleteView):
    model = Categoria
    success_url= '../categorias/'

class CatAdd(CreateView):
    model = Categoria
    fields = '__all__' 
    success_url = '../categorias/'

class AutorEdit(UpdateView):
    model = Autor
    fields= ['title']
    success_url= '../autores/' 

class AutorDelete(DeleteView):
    model = Autor
    success_url= '../autores/'

class AutorAdd(CreateView):
    model = Autor
    fields = '__all__' 
    success_url = '../autores/'