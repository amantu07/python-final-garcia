from django.urls import path
from Posts import views

urlpatterns = [
    path('', views.index,name='index'),
    path('buscar/', views.index,name='index'),
    path('<int:post_id>/',views.post_detail,name='post_detail'),
    path('contacto/', views.contacto,name='contacto'),
    path('nuevo_post/', views.nuevo_post,name='nuevo_post'),
            
]