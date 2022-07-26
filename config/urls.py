from django.contrib import admin
from django.urls import path, include
from dsweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dsweb/', include('dsweb.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),
]
