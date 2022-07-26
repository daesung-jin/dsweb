from django.urls import path
from . import views

app_name = 'dsweb'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:inquiry_id>/', views.detail, name='detail'),
    path('inquiry/create/', views.inquiry_create, name='inquiry_create'),
    path('main/', views.main, name='main'),
]
