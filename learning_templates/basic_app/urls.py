from django.urls import include, path
from basic_app import views

#Template Tagging
app_name = 'basic_app'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other')
]