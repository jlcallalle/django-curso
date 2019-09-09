''' Platzigram Views'''

from django.http import HttpResponse

# utilities
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs ')
    # return HttpResponse('Hola, Mundo! Django con Views')
    return HttpResponse('Oh, Hi! time server is {now}'.format(now=now))


def hi(request):
    # print(request)
    # import pdb; pdb.set_trace()
    # en consola: (Pdb) request.META, (Pdb) request, (Pdb) request.method, (Pdb) request.GET
    numbers = request.GET['numbers']
    return HttpResponse(str(numbers)) 

    #  http://localhost:8000/hi/?numbers=10,40,50,32 , ** Tarea es ordenar lista y que sea formato JSON