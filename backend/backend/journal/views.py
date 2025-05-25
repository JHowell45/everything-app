from django.shortcuts import render
from django.views import generic
from .models import JournalEntry

# Create your views here.
class IndexView(generic.ListView):
    template_name = "journal/index.html"
    context_object_name = "journal_entries"

    def get_queryset(self):
        return JournalEntry.objects.all()

def new_entry(request):
    pass