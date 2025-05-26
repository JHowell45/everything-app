from django.shortcuts import render
from django.views import generic

from pushups.models import Pushup


# Create your views here.
class IndexView(generic.ListView):
    template_name = "pushups/index.html"
    context_object_name = "pushups"

    def get_queryset(self):
        return Pushup.objects.all()
