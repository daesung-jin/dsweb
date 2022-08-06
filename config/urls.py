from django.contrib import admin
from django.urls import path, include
from dsweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dsweb/', include('dsweb.urls')),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),
]

handler404 = 'common.views.page_not_found'
handler500 = 'common.views.page_not_found'
