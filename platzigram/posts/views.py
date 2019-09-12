""" Posts Views"""

from django.http import HttpResponse

# Utilities
from datetime import datetime

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yesica Cortes',
        'timestamp' :  datetime.now().strftime('%m/%d/%Y'),
        'picture' : 'https://picsum.photos/id/10/200/300/?image=1036',
    },
    {
        'name': 'Via Lactea',
        'user': 'Yesica Cortes',
        'timestamp' :  datetime.now().strftime('%m/%d/%Y'),
        'picture' : 'https://picsum.photos/id/10/200/300/?image=1036',
    },
    {
        'name': 'Nuevo Auditorio',
        'user': 'Yesica Cortes',
        'timestamp' :  datetime.now().strftime('%m/%d/%Y'),
        'picture' : 'https://picsum.photos/id/10/200/300/?image=1036',
    }
]

def list_posts(request):
    """ Lista de post existentes"""
    #posts = [1, 2 ,4]
    content= []
    for post in posts:
        content.append("""
            <p/><strong>{name}</strong></p>
            <p/><small>{user}</small></p>
            <p/><strong>{timestamp}</strong></p>
            <p/><figure><img src="{picture}"> </figure></p>
        """.format(**post))
    return HttpResponse(str('<div>'.join(content)))