from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('community/', views.community, name='community'),
    path('resources/', views.resources, name='resources'),
    path('bio/<int:RST_pk>', views.bio, name='bio'),
    path('point_details/', views.point_detail, name='point_details'),
    path('point_results/', views.point_results, name='point_results'),
    path('total_points/', views.total_points, name='total_points'),
]