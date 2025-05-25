from django.shortcuts import render
from django.views import generic
from .models import JournalEntry

# Create your views here.
class IndexView(generic.ListView):
    model = JournalEntry
    template_name = "journal/index.html"

    def get_queryset(self):
        return JournalEntry.objects.all()