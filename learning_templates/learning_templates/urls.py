
from django.contrib import admin
from django.urls import include, path
from basic_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('basic_app/',include('basic_app.urls')),
    path('admin/', admin.site.urls),
]
