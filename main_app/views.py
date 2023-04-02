from django.shortcuts import render
from .models import Snowboard

# Create your views here.

def all_snowboards(request):
    snowboards = Snowboard.objects.all()
    return render(request, 'all_snowboards.html', {'snowboards': snowboards})

def snowboard_detail(request, pk)

def about(request):
    return render(request, 'about.html')

def all_snowboards(request):
    snowboards = [
        {'brand': 'Burton', 'model': 'Custom', 'size': '156', 'price': 599},
        {'brand': 'Lib Tech', 'model': 'Travis Rice Pro', 'size': '157', 'price': 649},
        {'brand': 'Never Summer', 'model': 'West', 'size': '154', 'price': 579},
        {'brand': 'Jones', 'model': 'Explorer', 'size': '159', 'price': 599},
        {'brand': 'Arbor', 'model': 'Draft', 'size': '152', 'price': 399},
    ]
    return render(request, 'all_snowboards.html', {'snowboards': snowboards})


