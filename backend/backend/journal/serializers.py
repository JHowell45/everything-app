from .models import JournalEntry
from rest_framework import serializers

class JournalEntrySerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JournalEntry
        fields = '__all__'