from .models import JournalEntry
from rest_framework import serializers


class JournalEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JournalEntry
        fields = ["entry_date", "entry_text"]
