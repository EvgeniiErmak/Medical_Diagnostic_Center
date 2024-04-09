# educational_resources/views.py

from django.shortcuts import render, get_object_or_404
from .models import Resource


def resources_list(request):
    resources = Resource.objects.all()
    return render(request, 'educational_resources/resources_list.html', {'resources': resources})


def resource_detail(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    return render(request, 'educational_resources/resource_detail.html', {'resource': resource})


def resource_detail_1(request):
    resource = get_object_or_404(Resource, pk=1)
    return render(request, 'educational_resources/resource_detail.html', {'resource': resource})


def resource_detail_2(request):
    resource = get_object_or_404(Resource, pk=2)
    return render(request, 'educational_resources/resource_detail.html', {'resource': resource})


def resource_detail_3(request):
    return render(request, 'educational_resources/resource_detail_3.html')


def resource_detail_4(request):
    return render(request, 'educational_resources/resource_detail_4.html')


def resource_detail_5(request):
    return render(request, 'educational_resources/resource_detail_5.html')
