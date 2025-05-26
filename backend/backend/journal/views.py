from .models import JournalEntry
import logging
from rest_framework import permissions, viewsets
from .serializers import JournalEntrySerializer


logger = logging.getLogger(__name__)

# Create your views here.
class JournalEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing, creating, and editing journal entries
    """
    queryset = JournalEntry.objects.all().order_by('entry_date')
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

