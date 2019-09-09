""" Platzigram URLs module """
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('Hola, Mundo! Django')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world)
]
