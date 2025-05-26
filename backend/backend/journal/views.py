from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .models import JournalEntry
import logging
from django.shortcuts import redirect
from django.utils import timezone
from .forms import EntryForm

logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(generic.ListView):
    template_name = "journal/index.html"
    context_object_name = "journal_entries"

    def get_queryset(self):
        return JournalEntry.objects.all()

def new_entry(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            entry_date = timezone.now().date()
            entry_text: str = form.cleaned_data.get("entry")
            if entry := JournalEntry.objects.filter(entry_date=entry_date).first():
                entry.entry_text += f"\n{entry_text}"
                entry.save()
            else:
                JournalEntry.objects.create(entry_text=entry_text, entry_date = timezone.now())
            return redirect("journal:index")
        else:
            return HttpResponse("Failed!")
    else:
        return HttpResponse("Not POST!")
