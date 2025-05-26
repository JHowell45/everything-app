from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from pushups.forms import PushupForm
from pushups.models import Pushup
import logging

logger = logging.getLogger(__name__)


# Create your views here.
class IndexView(generic.ListView):
    template_name = "pushups/index.html"
    context_object_name = "pushups"

    def get_queryset(self):
        return Pushup.objects.all()


def new_entry(request):
    if request.method == "POST":
        form = PushupForm(request.POST)
        if form.is_valid():
            logger.warning(form.cleaned_data)
            Pushup.objects.create(body_weight=form.cleaned_data["body_weight"], amount=form.cleaned_data["amount"],
                                  on_knees=form.cleaned_data["on_knees"] or False)
        else:
            logger.warning(form.errors)
    return redirect("pushups:index")
