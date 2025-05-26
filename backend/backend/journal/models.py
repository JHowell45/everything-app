from django.db import models

# Create your models here.
class JournalEntry(models.Model):
    entry_date = models.DateField(blank=False, null=False, db_index=True, unique=True)
    entry_text: str = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)