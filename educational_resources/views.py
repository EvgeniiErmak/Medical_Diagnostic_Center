# educational_resources/views.py

from django.shortcuts import render, get_object_or_404
from .models import Resource


def resources_list(request):
    resources = Resource.objects.all()
    return render(request, 'educational_resources/resources_list.html', {'resources': resources})


def resource_detail(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    return render(request, 'educational_resources/resource_detail.html', {'resource': resource})
