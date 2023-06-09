from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Snowboard

# Create your views here.

def index(request):
    snowboards = Snowboard.object.all()
    context = {'snowboards': snowboards}
    return render(request, 'snowboard/index.html', context)

def all_snowboards(request):
    snowboards = Snowboard.objects.all()
    return render(request, 'all_snowboards.html', {'snowboards': snowboards})

def snowboard_detail(request):
    snowboard = Snowboard.objects.get
    return render(request, 'snowboard_detail.html', )

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


class SbowboardCreateView(CreateView):
    model = Snowboard
    fields = ['brand', 'model', 'size', 'price']
    template_name = 'snowboard_form.html'

class SnowboardUpdateView(UpdateView):
    model = Snowboard
    fields = ['brand', 'model', 'length']
    template_name = 'snowboard_form.html'

class SnowboardDeleteView(DeleteView):
    model = Snowboard
    template_name = 'snowboard_confirm_delete.html'


def snowboarding_detail(request, pk):
    snowboarders = snowboarding.snowboarders.all()
    return render(request, 'snowboarding_detail.html', {'snowboarding': snowboarding, 'snowboarders': snowboarders})

def add_snowboarder(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        snowboarder = Snowboarder.objects.create(name=name, snowboarding=snowboarding)
        return redirect('snowboarding_detail', pk=snowboarding)
    return render(request, 'add_snowboarder.html', {'snowboarding': snowboarding})

class SnowboardBrandList(ListView):
    model = SnowboardBrand
    template_name = 'snowboard_brands.html'