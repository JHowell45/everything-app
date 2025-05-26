from django.db import models

TOP_WEIGHT_CALC: float = 0.6916
TOP_WEIGHT_KNEES_CALC: float = 0.5356
BOTTOM_WEIGHT_CALC: float = 0.7504
BOTTOM_WEIGHT_KNEES_CALC: float = 0.618

# Create your models here.
class Pushup(models.Model):
    body_weight: float = models.FloatField()
    amount: int = models.IntegerField()
    on_knees: bool = models.BooleanField()
    set_finished = models.DateTimeField(auto_now_add=True, null=False)

    def calculate_top_weight(self) -> float:
        """
        Calculate the est. true weight at the top of the pushup.
        """
        return self.body_weight * (TOP_WEIGHT_KNEES_CALC if self.on_knees else TOP_WEIGHT_CALC)

    def calculate_bottom_weight(self) -> float:
        """
        Calculate the est. true weight at the bottom of the pushup.
        """
        return self.body_weight * (BOTTOM_WEIGHT_KNEES_CALC if self.on_knees else BOTTOM_WEIGHT_CALC)

    def calculate_top_volume(self) -> float:
        """
        Calculate the est. true volume at the top of the pushup.
        """
        return self.calculate_top_weight() * self.amount

    def calculate_bottom_volume(self) -> float:
        """
        Calculate the est. true volume at the bottom of the pushup.
        """
        return self.calculate_bottom_weight() * self.amount
