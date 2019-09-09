""" Posts Views"""

from django.http import HttpResponse

# Utilities
from datetime import datetime

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yesica Cortes'
    }
]

def list_posts(request):
    posts = [1, 2 ,4]
    return HttpResponse(str(posts))