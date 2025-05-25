from django.db import models

# Create your models here.
class JournalEntry(models.Model):
    entry_date = models.DateField(blank=False, null=False)
    entry_text: str = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)