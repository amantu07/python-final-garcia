from django.urls import path
from Posts import views

urlpatterns = [
    path('', views.index,name='Home'),
    path('buscar/', views.buscar,name='buscar'),
    path('all_post/', views.all_post,name='AllPost'),
    path('categorias/', views.categorias,name='Categorias'),
    path('autores/', views.autores,name='Autores'),
    path('<int:post_id>/',views.post_detail,name='post_detail'),
    path('contacto/', views.contacto,name='contacto'),
    path('nuevo_post/', views.NuevoPost.as_view(),name='New'),
    path('post_edit/<pk>', views.PostEdit.as_view(),name='Edit'),
    path("post_delete/<pk>",views.PostDelete.as_view(),name='Delete'),
    path('comment_edit/<pk>', views.CommentEdit.as_view(),name='CommentEdit'),
    path("comment_delete/<pk>",views.CommentDelete.as_view(),name='CommentDelete'),
    path('category_edit/<pk>', views.CatEdit.as_view(),name='CatEdit'),
    path("category_delete/<pk>",views.CatDelete.as_view(),name='CatDelete'),    
    path("category_add/",views.CatAdd.as_view(),name='CatAdd'),     
    path("autor_add/",views.AutorAdd.as_view(),name='AutorAdd'),
    path('autor_edit/<pk>', views.AutorEdit.as_view(),name='AutorEdit'),
    path("autor_delete/<pk>",views.AutorDelete.as_view(),name='AutorDelete'),    
]