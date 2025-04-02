from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('<slug:entry_slug>/', views.entry_detail, name = 'entry_detail'),
]