from django.db import models

# Create your models here.
class Pushup(models.Model):
    body_weight: float = models.FloatField()
    amount: int = models.IntegerField()
    on_knees: bool = models.BooleanField()
    set_finished = models.DateTimeField(auto_now_add=True, null=False)
