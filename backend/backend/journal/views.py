from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .models import JournalEntry
import logging
from django.shortcuts import redirect
from django.utils import timezone
from .forms import EntryForm
from rest_framework import permissions, viewsets
logger = logging.getLogger(__name__)
from .serializers import JournalEntrySerialiser
# Create your views here.
class JournalEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing, creating, and editing journal entries
    """
    queryset = JournalEntry.objects.all().order_by('entry_date')
    serializer_class = JournalEntrySerialiser
    permission_classes = [permissions.IsAuthenticated]


