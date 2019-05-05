from django.http import HttpResponseRedirect
from django.shortcuts import render

from nav.utilites import handle_uploaded_file
from .models import Route, Path
from .forms import Routes


def home_page(request):
    return render(request, 'home.html', {'form': Routes(), 'routes': Route.objects.all()})


def upload(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = Routes(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])

    return HttpResponseRedirect('/nav/')


def route(request, route_id):
    paths = Path.objects.filter(route_id=route_id)
    return render(request, 'route.html', {'paths': paths, 'route': Route.objects.get(id=route_id)})


