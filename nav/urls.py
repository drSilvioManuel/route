from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('upload', views.upload, name='upload'),
    path('route/<int:route_id>', views.route, name='route'),
]
