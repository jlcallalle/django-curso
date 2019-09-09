''' Platzigram Views'''

from django.http import HttpResponse

# utilities
from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs ')
    # return HttpResponse('Hola, Mundo! Django con Views')
    return HttpResponse('Oh, Hi! time server is {now}'.format(now=now))


def sort_integers(request):
    # print(request)
    
    # en consola: (Pdb) request.META, (Pdb) request, (Pdb) request.method, (Pdb) request.GET
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    # import pdb; pdb.set_trace()
    # (Pdb) numbers
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
    )

    #  http://localhost:8000/hi/?numbers=10,40,50,32 , ** Tarea es ordenar lista y que sea formato JSON
    #  http://localhost:8000/sorted/?numbers=19,40,50,32




def say_hi(request, name, age):
    
    if age < 12:
        message = 'Sorry {}, no permitido'.format(name)
    else :
        message = 'Hello, {}! Welcome to platzigram'.format(name)
    
    return HttpResponse(message)
