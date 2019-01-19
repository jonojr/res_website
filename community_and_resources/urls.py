from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('community/', views.community, name='community'),
    path('resources/', views.resources, name='resources'),
    path('bio/<int:RST_pk>', views.bio, name='bio'),
]