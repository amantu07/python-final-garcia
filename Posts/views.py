from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.db.models import Q


def index(request):
    busqueda = request.GET.get("buscar")
    post = Post.objects.all()
    if busqueda:
        post= Post.objects.filter(
            Q(titulo__icontains = busqueda) |
            Q(contenido__icontains = busqueda)
        ).distinct
     
    return render(request, 'index.html', {'post':post})


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


def nuevo_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = form
            new_form.save()
            return HttpResponseRedirect('.')
    else:
        form = PostForm

    return render(request, 'nuevo_post.html', {'form':form})